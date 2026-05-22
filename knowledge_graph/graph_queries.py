# knowledge_graph/graph_queries.py
# Query interface over the NetworkX knowledge graph - used by the agent layer

import logging
from typing import Optional
import networkx as nx
from knowledge_graph.schema import CausalStrength, EdgeType, NodeType

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Node queries
# ---------------------------------------------------------------------------

def find_node_by_api_id(
    graph: nx.DiGraph,
    api_football_id: int,
    node_type: NodeType
) -> Optional[dict]:
    """
    Finds a node by its API-Football ID and node type.
    Returns node properties dict or None if not found.
    """
    for node_id, properties in graph.nodes(data=True):
        if (
            properties.get("api_football_id") == api_football_id
            and properties.get("node_type") == node_type.value
        ):
            return {"node_id": node_id, **properties}
    return None


def find_nodes_by_type(
    graph: nx.DiGraph,
    node_type: NodeType
) -> list[dict]:
    """
    Returns all nodes of a given type with their properties.
    """
    results = []
    for node_id, properties in graph.nodes(data=True):
        if properties.get("node_type") == node_type.value:
            results.append({"node_id": node_id, **properties})
    return results


def find_node_by_name(
    graph: nx.DiGraph,
    name: str,
    node_type: NodeType
) -> Optional[dict]:
    """
    Finds a node by name and type.
    Used when API ID is not available - name matching is case-insensitive.
    """
    name_lower = name.lower()
    for node_id, properties in graph.nodes(data=True):
        if (
            properties.get("node_type") == node_type.value
            and properties.get("name", "").lower() == name_lower
        ):
            return {"node_id": node_id, **properties}
    return None


def get_node_properties(
    graph: nx.DiGraph,
    node_id: str
) -> Optional[dict]:
    """
    Returns all properties of a node by its graph ID.
    Returns None if node does not exist.
    """
    if node_id not in graph:
        logger.warning(f"Node {node_id} not found in graph")
        return None
    return {"node_id": node_id, **graph.nodes[node_id]}


# ---------------------------------------------------------------------------
# Edge queries
# ---------------------------------------------------------------------------

def get_outgoing_edges(
    graph: nx.DiGraph,
    node_id: str,
    edge_type: Optional[EdgeType] = None
) -> list[dict]:
    """
    Returns all outgoing edges from a node.
    Optionally filters by edge type.
    """
    edges = []
    for _, to_id, properties in graph.out_edges(node_id, data=True):
        if edge_type is None or properties.get("edge_type") == edge_type.value:
            edges.append({
                "from_node_id": node_id,
                "to_node_id": to_id,
                **properties
            })
    return edges


def get_incoming_edges(
    graph: nx.DiGraph,
    node_id: str,
    edge_type: Optional[EdgeType] = None
) -> list[dict]:
    """
    Returns all incoming edges to a node.
    Optionally filters by edge type.
    """
    edges = []
    for from_id, _, properties in graph.in_edges(node_id, data=True):
        if edge_type is None or properties.get("edge_type") == edge_type.value:
            edges.append({
                "from_node_id": from_id,
                "to_node_id": node_id,
                **properties
            })
    return edges


# ---------------------------------------------------------------------------
# Causal edge queries
# ---------------------------------------------------------------------------

def get_causal_consequences(
    graph: nx.DiGraph,
    node_id: str,
    min_strength: CausalStrength = CausalStrength.LOW
) -> list[dict]:
    """
    Returns all causal consequences of a node filtered by minimum strength.
    Strength hierarchy: HIGH > MEDIUM > LOW.
    """
    strength_order = {
        CausalStrength.LOW.value: 0,
        CausalStrength.MEDIUM.value: 1,
        CausalStrength.HIGH.value: 2
    }
    min_level = strength_order[min_strength.value]

    consequences = []
    for _, to_id, properties in graph.out_edges(node_id, data=True):
        if properties.get("edge_type") != EdgeType.CAUSED.value:
            continue
        strength = properties.get("causal_strength", CausalStrength.LOW.value)
        if strength_order.get(strength, 0) >= min_level:
            consequences.append({
                "from_node_id": node_id,
                "to_node_id": to_id,
                **properties
            })

    consequences.sort(
        key=lambda e: strength_order.get(
            e.get("causal_strength", CausalStrength.LOW.value), 0
        ),
        reverse=True
    )
    return consequences


def get_causal_chain(
    graph: nx.DiGraph,
    node_id: str,
    depth: int = 3,
    min_strength: CausalStrength = CausalStrength.MEDIUM
) -> list[dict]:
    """
    Traverses causal edges from a node up to a given depth.
    Returns a flattened list of causal edges in traversal order.
    Used by the agent to understand downstream consequences of a divergence.
    """
    visited = set()
    chain = []

    def traverse(current_id: str, current_depth: int) -> None:
        if current_depth == 0 or current_id in visited:
            return
        visited.add(current_id)
        consequences = get_causal_consequences(graph, current_id, min_strength)
        for consequence in consequences:
            chain.append(consequence)
            traverse(consequence["to_node_id"], current_depth - 1)

    traverse(node_id, depth)
    return chain


# ---------------------------------------------------------------------------
# Divergence point queries
# ---------------------------------------------------------------------------

def find_match_node(
    graph: nx.DiGraph,
    team_a_name: str,
    team_b_name: str,
    tournament: str,
    season: int
) -> Optional[dict]:
    """
    Finds a specific match node by teams, tournament, and season.
    Used by the premise parser to locate the divergence point.
    Case-insensitive name matching on both home and away team.
    """
    team_a_lower = team_a_name.lower()
    team_b_lower = team_b_name.lower()
    tournament_lower = tournament.lower()

    for node_id, properties in graph.nodes(data=True):
        if properties.get("node_type") != NodeType.MATCH.value:
            continue
        home = properties.get("team_home_name", "").lower()
        away = properties.get("team_away_name", "").lower()
        t = properties.get("tournament", "").lower()
        s = properties.get("season")

        teams_match = (
            (home == team_a_lower and away == team_b_lower) or
            (home == team_b_lower and away == team_a_lower)
        )
        if teams_match and tournament_lower in t and s == season:
            return {"node_id": node_id, **properties}

    return None


def get_tournament_matches(
    graph: nx.DiGraph,
    tournament: str,
    season: int
) -> list[dict]:
    """
    Returns all match nodes for a given tournament and season.
    """
    tournament_lower = tournament.lower()
    matches = []

    for node_id, properties in graph.nodes(data=True):
        if properties.get("node_type") != NodeType.MATCH.value:
            continue
        if (
            tournament_lower in properties.get("tournament", "").lower()
            and properties.get("season") == season
        ):
            matches.append({"node_id": node_id, **properties})

    return sorted(matches, key=lambda m: m.get("date", ""))