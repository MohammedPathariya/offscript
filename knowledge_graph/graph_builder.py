# knowledge_graph/graph_builder.py
# Loads persisted knowledge graph from MongoDB into NetworkX at runtime startup

import logging
from typing import Optional
import networkx as nx
from pymongo import MongoClient
from pymongo.database import Database

logger = logging.getLogger(__name__)

# Module-level graph instance - built once, queried many times
_graph: Optional[nx.DiGraph] = None


def build_graph(db: Database) -> nx.DiGraph:
    """
    Loads all nodes and edges from MongoDB into a NetworkX directed graph.
    Called once at application startup.
    """
    graph = nx.DiGraph()

    _load_nodes(graph, db)
    _load_edges(graph, db)
    _load_causal_edges(graph, db)

    logger.info(
        f"Knowledge graph built: {graph.number_of_nodes()} nodes, "
        f"{graph.number_of_edges()} edges"
    )
    return graph


def get_graph() -> nx.DiGraph:
    """
    Returns the module-level graph instance.
    Raises RuntimeError if graph has not been initialized yet.
    """
    if _graph is None:
        raise RuntimeError(
            "Knowledge graph not initialized. Call init_graph() first."
        )
    return _graph


def init_graph(db: Database) -> None:
    """
    Builds the graph and stores it as the module-level instance.
    This is the entry point called by the Flask app at startup.
    """
    global _graph
    _graph = build_graph(db)


def _load_nodes(graph: nx.DiGraph, db: Database) -> None:
    """Loads all node documents from MongoDB into the graph."""
    nodes = db["nodes"].find({})
    count = 0

    for node in nodes:
        node_id = str(node["_id"])
        properties = {k: v for k, v in node.items() if k != "_id"}
        graph.add_node(node_id, **properties)
        count += 1

    logger.info(f"Loaded {count} nodes")


def _load_edges(graph: nx.DiGraph, db: Database) -> None:
    """Loads all standard edge documents from MongoDB into the graph."""
    edges = db["edges"].find({})
    count = 0

    for edge in edges:
        from_id = edge["from_node_id"]
        to_id = edge["to_node_id"]
        properties = {
            k: v for k, v in edge.items()
            if k not in ("_id", "from_node_id", "to_node_id")
        }
        graph.add_edge(from_id, to_id, **properties)
        count += 1

    logger.info(f"Loaded {count} standard edges")


def _load_causal_edges(graph: nx.DiGraph, db: Database) -> None:
    """Loads all causal edge documents from MongoDB into the graph."""
    causal_edges = db["causal_edges"].find({})
    count = 0

    for edge in causal_edges:
        from_id = edge["from_node_id"]
        to_id = edge["to_node_id"]
        properties = {
            k: v for k, v in edge.items()
            if k not in ("_id", "from_node_id", "to_node_id")
        }
        graph.add_edge(from_id, to_id, **properties)
        count += 1

    logger.info(f"Loaded {count} causal edges")