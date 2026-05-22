# knowledge_graph/schema.py
# Defines all node and edge type structures for the OffScript knowledge graph

from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class NodeType(str, Enum):
    PLAYER = "player"
    MANAGER = "manager"
    NATIONAL_TEAM = "national_team"
    CLUB_TEAM = "club_team"
    TOURNAMENT = "tournament"
    MATCH = "match"
    CAREER_EVENT = "career_event"


class EdgeType(str, Enum):
    PLAYED_IN = "PLAYED_IN"
    TRANSFERRED_TO = "TRANSFERRED_TO"
    COMPETED_IN = "COMPETED_IN"
    HAS_EVENT = "HAS_EVENT"
    MANAGED_BY = "MANAGED_BY"
    SELECTED = "SELECTED"
    PARTICIPATED_IN = "PARTICIPATED_IN"
    CONTAINS = "CONTAINS"
    CAUSED = "CAUSED"


class CausalStrength(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class MatchDecidedBy(str, Enum):
    FULL_TIME = "FT"
    EXTRA_TIME = "ET"
    PENALTIES = "PEN"


class TransferType(str, Enum):
    FEE = "fee"
    FREE = "free"
    LOAN = "loan"
    
class ReasoningMode(str, Enum):
    GROUNDED = "grounded"
    SPECULATIVE = "speculative"
    CREATIVE = "creative"


# ---------------------------------------------------------------------------
# Sub-structures
# ---------------------------------------------------------------------------

@dataclass
class Score:
    home: Optional[int]
    away: Optional[int]


@dataclass
class SeasonStats:
    season: int
    league_id: int
    league_name: str
    team_id: int
    team_name: str
    appearances: int
    minutes: int
    goals: int
    assists: int
    rating: Optional[float]
    yellow_cards: int
    red_cards: int


@dataclass
class ManagementEntry:
    team_id: int
    team_name: str
    start_date: str
    end_date: Optional[str]  # None means current role


# ---------------------------------------------------------------------------
# Node types
# ---------------------------------------------------------------------------

@dataclass
class PlayerNode:
    node_type: NodeType = field(default=NodeType.PLAYER, init=False)
    api_football_id: int
    name: str
    nationality: str
    date_of_birth: str
    position: str
    height: Optional[str]
    weight: Optional[str]
    international_caps: int
    international_goals: int
    major_honors: list[str]
    season_stats: list[SeasonStats]


@dataclass
class ManagerNode:
    node_type: NodeType = field(default=NodeType.MANAGER, init=False)
    api_football_id: int
    name: str
    nationality: str
    date_of_birth: str
    tactical_style: Optional[str]       # sourced from Wikipedia
    management_timeline: list[ManagementEntry]
    major_honors: list[str]


@dataclass
class NationalTeamNode:
    node_type: NodeType = field(default=NodeType.NATIONAL_TEAM, init=False)
    api_football_id: int
    nation: str
    fifa_ranking: Optional[int]
    typical_formation: Optional[str]
    playing_style: Optional[str]
    historical_wc_results: list[str]


@dataclass
class ClubTeamNode:
    node_type: NodeType = field(default=NodeType.CLUB_TEAM, init=False)
    api_football_id: int
    club_name: str
    league: str
    country: str
    ucl_results_2018_2023: list[str]
    key_players_per_season: list[str]


@dataclass
class TournamentNode:
    node_type: NodeType = field(default=NodeType.TOURNAMENT, init=False)
    api_football_id: int
    name: str
    year: int
    host_nation: str
    winner: Optional[str]
    runner_up: Optional[str]
    top_scorer: Optional[str]
    golden_ball_winner: Optional[str]


@dataclass
class MatchNode:
    node_type: NodeType = field(default=NodeType.MATCH, init=False)
    api_football_id: int
    tournament: str
    season: int
    stage: str
    date: str
    team_home_id: int
    team_home_name: str
    team_away_id: int
    team_away_name: str
    winner_team_id: Optional[int]
    score_halftime: Score
    score_fulltime: Score
    score_extratime: Score
    score_penalties: Score
    decided_by: MatchDecidedBy
    referee: Optional[str]
    venue: Optional[str]


@dataclass
class CareerEventNode:
    node_type: NodeType = field(default=NodeType.CAREER_EVENT, init=False)
    player_id: int
    player_name: str
    date: str
    transfer_type: TransferType
    fee: Optional[str]
    from_team_id: int
    from_team_name: str
    to_team_id: int
    to_team_name: str


# ---------------------------------------------------------------------------
# Edge types
# ---------------------------------------------------------------------------

@dataclass
class GraphEdge:
    edge_type: EdgeType
    from_node_id: str
    to_node_id: str
    properties: dict = field(default_factory=dict)


@dataclass
class CausalEdge:
    edge_type: EdgeType = field(default=EdgeType.CAUSED, init=False)
    from_node_id: str
    to_node_id: str
    causal_strength: CausalStrength
    consequence_type: str
    reasoning: str