# knowledge_graph/causal_edges.py
# Manually curated causal edge definitions - ground truth for the consistency checker
# Expanded with domain expertise across 2018/2022 World Cups and UCL 2018-2023
# These are never auto-generated - each edge is deliberately reasoned and validated

from knowledge_graph.schema import CausalEdge, CausalStrength, EdgeType


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _edge(
    from_node_id: str,
    to_node_id: str,
    strength: CausalStrength,
    consequence_type: str,
    reasoning: str
) -> CausalEdge:
    return CausalEdge(
        from_node_id=from_node_id,
        to_node_id=to_node_id,
        causal_strength=strength,
        consequence_type=consequence_type,
        reasoning=reasoning
    )


# ---------------------------------------------------------------------------
# Fixed timeline nodes - events that occur regardless of World Cup results
# ---------------------------------------------------------------------------

FIXED_TIMELINE_NODES: list[dict] = [
    {
        "node_id": "transfer_mbappe_realmadrid_2024",
        "description": "Mbappe transfers to Real Madrid in 2024 on a free transfer.",
        "reasoning": "Lifelong Real Madrid fan, PSG structurally failing in UCL, "
                     "move was inevitable regardless of World Cup results."
    },
    {
        "node_id": "transfer_messi_intermiami_2023",
        "description": "Messi moves to Inter Miami in 2023.",
        "reasoning": "Career wind down move decided independently of World Cup outcomes."
    },
    {
        "node_id": "psg_ucl_failure_2018_2024",
        "description": "PSG fails to win the Champions League between 2018 and 2024.",
        "reasoning": "Structural squad imbalance and tactical problems persist "
                     "regardless of World Cup results."
    },
    {
        "node_id": "transfer_ronaldo_juventus_2018",
        "description": "Ronaldo transfers to Juventus in 2018.",
        "reasoning": "Decision made before World Cup, driven by desire for Serie A "
                     "challenge and Juventus pursuit."
    },
    {
        "node_id": "transfer_neymar_psg_2017",
        "description": "Neymar transfers to PSG in 2017 for world record fee.",
        "reasoning": "Transfer completed before 2018 World Cup cycle began."
    },
]


# ---------------------------------------------------------------------------
# Real timeline - 2018 World Cup consequences
# ---------------------------------------------------------------------------

REAL_2018_CAUSAL_EDGES: list[CausalEdge] = [

    # France
    _edge(
        "tournament_wc_2018",
        "manager_deschamps",
        CausalStrength.HIGH,
        "legacy",
        "Winning 2018 establishes Deschamps as an elite international manager, "
        "securing his position and legacy with France."
    ),
    _edge(
        "tournament_wc_2018",
        "player_mbappe",
        CausalStrength.HIGH,
        "legacy",
        "Winning the World Cup at 19 cements the generational talent narrative "
        "around Mbappe immediately."
    ),
    _edge(
        "tournament_wc_2018",
        "player_pogba",
        CausalStrength.MEDIUM,
        "legacy",
        "2018 represents Pogba's peak moment internationally, setting "
        "expectations his club career never quite matches."
    ),

    # Croatia
    _edge(
        "national_team_croatia_wc2018_final",
        "player_modric",
        CausalStrength.HIGH,
        "legacy",
        "Reaching the final as captain directly leads to Modric winning "
        "the 2018 Ballon d'Or, breaking the Messi-Ronaldo duopoly."
    ),
    _edge(
        "national_team_croatia_wc2018_final",
        "national_team_croatia",
        CausalStrength.HIGH,
        "legacy",
        "Reaching the final marks the undisputed peak of Croatia's "
        "golden generation."
    ),
    _edge(
        "national_team_croatia_wc2018_final",
        "player_rakitic",
        CausalStrength.MEDIUM,
        "legacy",
        "The 2018 final represents Rakitic's peak international moment "
        "alongside Modric."
    ),

    # Belgium
    _edge(
        "national_team_belgium_wc2018_3rd",
        "national_team_belgium",
        CausalStrength.HIGH,
        "legacy",
        "Third place is the golden generation's best World Cup result, "
        "defining what this squad achieves collectively."
    ),
    _edge(
        "national_team_belgium_wc2018_3rd",
        "player_debruyne",
        CausalStrength.MEDIUM,
        "legacy",
        "Belgium's run helps establish De Bruyne as one of the world's "
        "best midfielders on the international stage."
    ),
    _edge(
        "national_team_belgium_wc2018_3rd",
        "player_lukaku",
        CausalStrength.MEDIUM,
        "legacy",
        "Lukaku's goals in 2018 represent his international reputation peak "
        "before club form becomes inconsistent."
    ),
    _edge(
        "national_team_belgium_wc2018_3rd",
        "player_hazard",
        CausalStrength.MEDIUM,
        "legacy",
        "2018 is Hazard's last great tournament before his Real Madrid move "
        "and subsequent injury decline."
    ),

    # Brazil
    _edge(
        "national_team_brazil_wc2018_exit",
        "player_neymar",
        CausalStrength.HIGH,
        "legacy",
        "Brazil's quarterfinal exit continues Neymar's World Cup heartbreak "
        "narrative, adding pressure on his PSG project."
    ),
    _edge(
        "national_team_brazil_wc2018_exit",
        "manager_tite",
        CausalStrength.MEDIUM,
        "legacy",
        "Quarterfinal exit begins questions about Tite's tactical approach "
        "at major tournaments."
    ),
    _edge(
        "national_team_brazil_wc2018_exit",
        "player_coutinho",
        CausalStrength.LOW,
        "legacy",
        "Coutinho's best international moment passes without a major trophy "
        "to show for it."
    ),

    # England
    _edge(
        "national_team_england_wc2018_sf",
        "manager_southgate",
        CausalStrength.HIGH,
        "legacy",
        "Reaching the semifinals establishes Southgate era credibility "
        "and begins the Young Lions narrative."
    ),
    _edge(
        "national_team_england_wc2018_sf",
        "player_kane",
        CausalStrength.HIGH,
        "legacy",
        "Kane wins the 2018 Golden Boot, establishing himself as a world "
        "class striker on the global stage."
    ),
    _edge(
        "national_team_england_wc2018_sf",
        "national_team_england",
        CausalStrength.MEDIUM,
        "legacy",
        "Semifinal finish begins the Young Lions narrative that defines "
        "England's next tournament cycle."
    ),

    # Germany
    _edge(
        "national_team_germany_wc2018_exit",
        "manager_low",
        CausalStrength.HIGH,
        "legacy",
        "Group stage exit is Germany's worst World Cup result in decades, "
        "directly leading to Low's eventual sacking."
    ),
    _edge(
        "national_team_germany_wc2018_exit",
        "player_ozil",
        CausalStrength.HIGH,
        "legacy",
        "Group stage exit triggers the Ozil racism controversy and his "
        "retirement from international football."
    ),
    _edge(
        "national_team_germany_wc2018_exit",
        "national_team_germany",
        CausalStrength.HIGH,
        "legacy",
        "Group stage exit triggers a painful generational rebuild that "
        "defines German football for years."
    ),

    # Russia
    _edge(
        "national_team_russia_wc2018_qf",
        "national_team_russia",
        CausalStrength.MEDIUM,
        "legacy",
        "Host nation exceeding all expectations by reaching the quarterfinals "
        "creates a brief golden moment for Russian football."
    ),
    _edge(
        "national_team_russia_wc2018_qf",
        "player_cheryshev",
        CausalStrength.LOW,
        "legacy",
        "Cheryshev emerges as the tournament's surprise revelation with "
        "four goals from the bench."
    ),
]


# ---------------------------------------------------------------------------
# Real timeline - 2022 World Cup consequences
# ---------------------------------------------------------------------------

REAL_2022_CAUSAL_EDGES: list[CausalEdge] = [

    # Argentina
    _edge(
        "tournament_wc_2022",
        "player_messi",
        CausalStrength.HIGH,
        "legacy",
        "Winning 2022 resolves the GOAT debate for most of the football world. "
        "Messi now has every major trophy available to him."
    ),
    _edge(
        "tournament_wc_2022",
        "player_dimaria",
        CausalStrength.MEDIUM,
        "legacy",
        "Di Maria wins a World Cup in what is effectively his farewell "
        "tournament for Argentina, completing his international legacy."
    ),
    _edge(
        "tournament_wc_2022",
        "manager_scaloni",
        CausalStrength.HIGH,
        "legacy",
        "Winning 2022 establishes Scaloni as a world class manager despite "
        "his lack of experience before taking the Argentina job."
    ),

    # France
    _edge(
        "national_team_france_wc2022_final",
        "player_mbappe",
        CausalStrength.MEDIUM,
        "legacy",
        "Mbappe wins the Golden Boot despite France losing the final, "
        "paradoxically strengthening his individual legacy."
    ),
    _edge(
        "national_team_france_wc2022_final",
        "player_giroud",
        CausalStrength.LOW,
        "legacy",
        "Giroud's all time France top scorer record is overshadowed by "
        "the final defeat, reducing the milestone's cultural impact."
    ),

    # Morocco
    _edge(
        "national_team_morocco_wc2022_sf",
        "national_team_morocco",
        CausalStrength.HIGH,
        "legacy",
        "First African nation to reach a World Cup semifinal, permanently "
        "elevating African and Arab football credibility."
    ),
    _edge(
        "national_team_morocco_wc2022_sf",
        "player_hakimi",
        CausalStrength.HIGH,
        "legacy",
        "Hakimi's performances earn him global recognition as one of the "
        "world's best fullbacks."
    ),
    _edge(
        "national_team_morocco_wc2022_sf",
        "player_amrabat",
        CausalStrength.HIGH,
        "legacy",
        "Amrabat's midfield dominance throughout the tournament leads "
        "directly to elite club interest and a Manchester United move."
    ),
    _edge(
        "national_team_morocco_wc2022_sf",
        "manager_regragui",
        CausalStrength.MEDIUM,
        "legacy",
        "Regragui established as a top international manager after taking "
        "Morocco to the semifinals in his first major tournament."
    ),
    _edge(
        "national_team_morocco_wc2022_sf",
        "player_ziyech",
        CausalStrength.MEDIUM,
        "transfer",
        "Ziyech's tournament performances spike his transfer market value "
        "despite his difficult Chelsea situation."
    ),

    # Brazil
    _edge(
        "national_team_brazil_wc2022_exit",
        "player_neymar",
        CausalStrength.HIGH,
        "legacy",
        "Brazil's quarterfinal exit continues Neymar's World Cup heartbreak "
        "narrative for a second consecutive tournament."
    ),
    _edge(
        "national_team_brazil_wc2022_exit",
        "manager_tite",
        CausalStrength.HIGH,
        "legacy",
        "Tite resigns immediately after the quarterfinal exit, ending his "
        "Brazil tenure on a painful note."
    ),
    _edge(
        "national_team_brazil_wc2022_exit",
        "player_vinicius",
        CausalStrength.HIGH,
        "legacy",
        "Brazil's exit accelerates Vinicius Jr inheriting the torch as "
        "Brazil's next generational star."
    ),
    _edge(
        "national_team_brazil_wc2022_exit",
        "player_richarlison",
        CausalStrength.MEDIUM,
        "legacy",
        "Richarlison has a golden personal tournament including a bicycle "
        "kick goal despite Brazil's team exit."
    ),
    _edge(
        "national_team_brazil_wc2022_exit",
        "national_team_brazil",
        CausalStrength.MEDIUM,
        "legacy",
        "CBF begins a painful generational transition following back to back "
        "quarterfinal exits."
    ),

    # England
    _edge(
        "national_team_england_wc2022_exit",
        "manager_southgate",
        CausalStrength.HIGH,
        "legacy",
        "Quarterfinal exit begins the feeling that the Southgate era has "
        "reached its ceiling."
    ),
    _edge(
        "national_team_england_wc2022_exit",
        "player_bellingham",
        CausalStrength.HIGH,
        "legacy",
        "Bellingham announces himself as England's next talisman with a "
        "commanding tournament at just 19."
    ),
    _edge(
        "national_team_england_wc2022_exit",
        "player_kane",
        CausalStrength.MEDIUM,
        "legacy",
        "Kane's missed penalty in the quarterfinal shootout adds a question "
        "mark to his international legacy."
    ),
    _edge(
        "national_team_england_wc2022_exit",
        "manager_southgate",
        CausalStrength.MEDIUM,
        "legacy",
        "Southgate resignation conversation begins seriously after the "
        "quarterfinal exit."
    ),

    # Netherlands
    _edge(
        "national_team_netherlands_wc2022_qf",
        "manager_vangaal",
        CausalStrength.HIGH,
        "legacy",
        "Van Gaal coaches his farewell tournament while battling illness, "
        "reaching the quarterfinals in a dignified exit."
    ),
    _edge(
        "national_team_netherlands_wc2022_qf",
        "player_gakpo",
        CausalStrength.HIGH,
        "legacy",
        "Gakpo's three group stage goals announce him as a world class "
        "attacker, directly triggering his Liverpool transfer."
    ),
    _edge(
        "national_team_netherlands_wc2022_qf",
        "player_vandijk",
        CausalStrength.MEDIUM,
        "legacy",
        "Van Dijk leads Netherlands to the quarterfinals in what represents "
        "his peak international moment."
    ),

    # Portugal
    _edge(
        "national_team_portugal_wc2022_exit",
        "player_ronaldo",
        CausalStrength.HIGH,
        "legacy",
        "Ronaldo being benched by Santos creates the defining controversy "
        "of his final World Cup, ending his international career on "
        "a sour note."
    ),
    _edge(
        "national_team_portugal_wc2022_exit",
        "manager_santos",
        CausalStrength.HIGH,
        "legacy",
        "Fernando Santos sacked immediately after the quarterfinal exit "
        "following the Ronaldo benching controversy."
    ),
    _edge(
        "national_team_portugal_wc2022_exit",
        "player_ronaldo",
        CausalStrength.HIGH,
        "legacy",
        "Quarterfinal exit triggers serious uncertainty around Ronaldo's "
        "international future and eventual retirement from Portugal."
    ),
    _edge(
        "national_team_portugal_wc2022_exit",
        "player_felix",
        CausalStrength.MEDIUM,
        "legacy",
        "Felix and Leao's performances signal the next generation torch "
        "being passed in Portuguese football."
    ),
    _edge(
        "national_team_portugal_wc2022_exit",
        "player_pepe",
        CausalStrength.LOW,
        "legacy",
        "Pepe plays his farewell tournament at 39, cementing his status "
        "as one of Portugal's greatest defenders."
    ),

    # Croatia
    _edge(
        "national_team_croatia_wc2022_3rd",
        "player_modric",
        CausalStrength.HIGH,
        "legacy",
        "Modric leads Croatia to back to back top four World Cup finishes, "
        "fully cementing his legacy as one of football's all time greats."
    ),
    _edge(
        "national_team_croatia_wc2022_3rd",
        "player_gvardiol",
        CausalStrength.HIGH,
        "legacy",
        "Gvardiol's performances announce him as the world's best young "
        "defender, triggering elite club interest."
    ),
    _edge(
        "national_team_croatia_wc2022_3rd",
        "national_team_croatia",
        CausalStrength.MEDIUM,
        "legacy",
        "Back to back top four finishes confirm Croatia's golden generation "
        "as one of the greatest in World Cup history."
    ),

    # Senegal
    _edge(
        "national_team_senegal_wc2022_exit",
        "player_mane",
        CausalStrength.HIGH,
        "legacy",
        "Mane's injury ruins Senegal's tournament, his absence directly "
        "contributing to their round of 16 exit."
    ),
    _edge(
        "national_team_senegal_wc2022_exit",
        "national_team_senegal",
        CausalStrength.MEDIUM,
        "legacy",
        "Senegal's exit shifts the African football narrative firmly "
        "toward Morocco's historic run."
    ),

    # Japan
    _edge(
        "national_team_japan_wc2022",
        "national_team_japan",
        CausalStrength.HIGH,
        "legacy",
        "Topping a group containing Germany and Spain is Japan's greatest "
        "ever World Cup group stage achievement."
    ),
    _edge(
        "national_team_japan_wc2022",
        "national_team_japan",
        CausalStrength.HIGH,
        "legacy",
        "Japan's group stage victories alongside Morocco's run create a "
        "surge in Asian and African football credibility globally."
    ),

    # Germany
    _edge(
        "national_team_germany_wc2022_exit",
        "manager_flick",
        CausalStrength.HIGH,
        "legacy",
        "Second consecutive group stage exit puts Hansi Flick's position "
        "under serious question."
    ),
    _edge(
        "national_team_germany_wc2022_exit",
        "player_muller",
        CausalStrength.HIGH,
        "legacy",
        "Group stage exit definitively ends the Muller and Neuer "
        "international era."
    ),
    _edge(
        "national_team_germany_wc2022_exit",
        "player_musiala",
        CausalStrength.MEDIUM,
        "legacy",
        "Germany's failure accelerates the transition to Musiala and "
        "Gnabry as the next generation leaders."
    ),

    # Spain
    _edge(
        "national_team_spain_wc2022_exit",
        "manager_luisenrique",
        CausalStrength.HIGH,
        "legacy",
        "Round of 16 exit ends the Luis Enrique era with Spain."
    ),
    _edge(
        "national_team_spain_wc2022_exit",
        "player_degea",
        CausalStrength.MEDIUM,
        "legacy",
        "De Gea's penalty shootout howler effectively ends his Spain "
        "international career."
    ),
    _edge(
        "national_team_spain_wc2022_exit",
        "player_pedri",
        CausalStrength.MEDIUM,
        "legacy",
        "Pedri and Gavi's performances show promise but the exit signals "
        "they need more tournament experience."
    ),
]


# ---------------------------------------------------------------------------
# Real timeline - Champions League 2018-2023 consequences
# ---------------------------------------------------------------------------

REAL_UCL_CAUSAL_EDGES: list[CausalEdge] = [

    # 2017-18 Real Madrid
    _edge(
        "ucl_2018_realmadrid",
        "player_ronaldo",
        CausalStrength.HIGH,
        "transfer",
        "Winning a third consecutive UCL gives Ronaldo the perfect moment "
        "to leave Real Madrid for Juventus, feeling his legacy is complete."
    ),
    _edge(
        "ucl_2018_realmadrid",
        "player_salah",
        CausalStrength.HIGH,
        "legacy",
        "Salah's injury in the final at Ramos's hands changes the trajectory "
        "of his peak season and fuels his 2018-19 revenge narrative."
    ),
    _edge(
        "ucl_2018_realmadrid",
        "player_bale",
        CausalStrength.MEDIUM,
        "legacy",
        "Bale's bicycle kick in the final represents his Real Madrid peak "
        "before his relationship with the club collapses."
    ),
    _edge(
        "ucl_2018_realmadrid",
        "manager_zidane",
        CausalStrength.HIGH,
        "legacy",
        "Zidane resigns at the peak of his managerial career having won "
        "three consecutive UCL titles."
    ),
    _edge(
        "ucl_2018_realmadrid",
        "player_karius",
        CausalStrength.HIGH,
        "legacy",
        "Karius's two howlers in the final effectively end his career "
        "at the elite level."
    ),

    # 2018-19 Liverpool
    _edge(
        "ucl_2019_liverpool",
        "player_salah",
        CausalStrength.HIGH,
        "legacy",
        "Salah winning the UCL with Liverpool completes his redemption "
        "narrative from the 2018 final injury."
    ),
    _edge(
        "ucl_2019_liverpool",
        "player_vandijk",
        CausalStrength.HIGH,
        "legacy",
        "Liverpool's defensive record throughout the UCL run confirms "
        "Van Dijk as the world's best defender."
    ),
    _edge(
        "ucl_2019_liverpool",
        "player_alisson",
        CausalStrength.HIGH,
        "legacy",
        "Alisson's performances confirm him as the world's best goalkeeper "
        "just one season after joining Liverpool."
    ),
    _edge(
        "ucl_2019_liverpool",
        "club_barcelona",
        CausalStrength.HIGH,
        "legacy",
        "Barcelona's collapse from 3-0 up in the semifinal directly ends "
        "the Valverde era at the club."
    ),
    _edge(
        "ucl_2019_liverpool",
        "player_firmino",
        CausalStrength.MEDIUM,
        "legacy",
        "Firmino's selfless no goal final perfectly defines his legacy "
        "as the ultimate team player."
    ),

    # 2019-20 Bayern Munich
    _edge(
        "ucl_2020_bayern",
        "player_lewandowski",
        CausalStrength.HIGH,
        "legacy",
        "Lewandowski's peak season goes without a Ballon d'Or due to "
        "COVID cancellation, one of football's great injustices."
    ),
    _edge(
        "ucl_2020_bayern",
        "manager_flick",
        CausalStrength.HIGH,
        "legacy",
        "Flick's treble in his first full season establishes him as "
        "one of the world's elite managers."
    ),
    _edge(
        "ucl_2020_bayern",
        "club_psg",
        CausalStrength.HIGH,
        "legacy",
        "PSG reaching the final with Mbappe and Neymar represents their "
        "closest moment to UCL glory under the QSI ownership."
    ),
    _edge(
        "ucl_2020_bayern",
        "player_kimmich",
        CausalStrength.MEDIUM,
        "legacy",
        "Kimmich's role in Bayern's treble establishes him as a world "
        "class midfielder transitioning from fullback."
    ),

    # 2020-21 Chelsea
    _edge(
        "ucl_2021_chelsea",
        "manager_tuchel",
        CausalStrength.HIGH,
        "legacy",
        "Tuchel winning the UCL within months of joining Chelsea confirms "
        "him as one of the world's elite managers."
    ),
    _edge(
        "ucl_2021_chelsea",
        "player_havertz",
        CausalStrength.HIGH,
        "legacy",
        "Havertz's winning goal in the final defines his Chelsea legacy "
        "and justifies his transfer fee."
    ),
    _edge(
        "ucl_2021_chelsea",
        "manager_guardiola",
        CausalStrength.HIGH,
        "legacy",
        "Man City reaching the final and losing reinforces the Guardiola "
        "UCL curse narrative at its peak."
    ),
    _edge(
        "ucl_2021_chelsea",
        "player_kante",
        CausalStrength.MEDIUM,
        "legacy",
        "Kante's dominant final performance represents the last time he "
        "is seen at this level before injuries take hold."
    ),

    # 2021-22 Real Madrid
    _edge(
        "ucl_2022_realmadrid",
        "player_benzema",
        CausalStrength.HIGH,
        "legacy",
        "Benzema's hat tricks against PSG and Chelsea, plus his final "
        "performance, directly lead to his 2022 Ballon d'Or."
    ),
    _edge(
        "ucl_2022_realmadrid",
        "player_vinicius",
        CausalStrength.HIGH,
        "legacy",
        "Vinicius's final winning goal announces him as the next "
        "Ballon d'Or contender."
    ),
    _edge(
        "ucl_2022_realmadrid",
        "player_courtois",
        CausalStrength.HIGH,
        "legacy",
        "Courtois's final performance is widely considered the greatest "
        "individual goalkeeping display in UCL final history."
    ),
    _edge(
        "ucl_2022_realmadrid",
        "player_salah",
        CausalStrength.HIGH,
        "legacy",
        "Liverpool reaching the final marks the end of the Salah and Mane "
        "partnership, with Mane leaving immediately after."
    ),
    _edge(
        "ucl_2022_realmadrid",
        "player_modric",
        CausalStrength.MEDIUM,
        "legacy",
        "Modric winning the UCL at 36 adds further evidence to his case "
        "as the greatest midfielder of his generation."
    ),

    # 2022-23 Manchester City
    _edge(
        "ucl_2023_mancity",
        "manager_guardiola",
        CausalStrength.HIGH,
        "legacy",
        "Guardiola finally breaks his UCL curse with City, silencing the "
        "biggest criticism of his managerial legacy."
    ),
    _edge(
        "ucl_2023_mancity",
        "player_haaland",
        CausalStrength.HIGH,
        "legacy",
        "Haaland's treble season with UCL glory definitively announces "
        "him as the dominant striker of his generation."
    ),
    _edge(
        "ucl_2023_mancity",
        "player_debruyne",
        CausalStrength.HIGH,
        "legacy",
        "De Bruyne's peak season contribution before injuries finally "
        "earns him a UCL winners medal."
    ),
    _edge(
        "ucl_2023_mancity",
        "player_rodri",
        CausalStrength.HIGH,
        "legacy",
        "Rodri's performances across the treble season cement him as "
        "the world's best defensive midfielder."
    ),
    _edge(
        "ucl_2023_mancity",
        "manager_guardiola",
        CausalStrength.HIGH,
        "legacy",
        "The treble solidifies Guardiola's legacy as the greatest manager "
        "in football history for most observers."
    ),
]


# ---------------------------------------------------------------------------
# Individual player causal edges
# ---------------------------------------------------------------------------

PLAYER_CAUSAL_EDGES: list[CausalEdge] = [

    # Ronaldo
    _edge(
        "player_ronaldo",
        "club_juventus",
        CausalStrength.HIGH,
        "transfer",
        "Ronaldo's Juventus move begins a Serie A dominance period but "
        "his UCL dream with them never materialises."
    ),
    _edge(
        "player_ronaldo_juventus",
        "national_team_portugal",
        CausalStrength.MEDIUM,
        "legacy",
        "Playing in Serie A reduces Ronaldo's visibility on the Champions "
        "League stage during his peak international years."
    ),
    _edge(
        "player_ronaldo_wc2022_benched",
        "player_ronaldo",
        CausalStrength.HIGH,
        "legacy",
        "Being benched by Santos creates the defining controversy of "
        "Ronaldo's final World Cup, ending his international career "
        "on a sour note."
    ),
    _edge(
        "player_ronaldo_saudi_2023",
        "player_ronaldo",
        CausalStrength.HIGH,
        "legacy",
        "Ronaldo's Saudi Arabia move definitively closes his European "
        "elite chapter."
    ),

    # Neymar
    _edge(
        "player_neymar_psg",
        "club_barcelona",
        CausalStrength.HIGH,
        "transfer",
        "Neymar's departure triggers Barcelona's painful rebuild and "
        "their eventual financial crisis."
    ),
    _edge(
        "player_neymar_ucl2020_final",
        "player_neymar",
        CausalStrength.HIGH,
        "legacy",
        "Reaching the UCL final with PSG is the closest Neymar ever gets "
        "to winning the competition in Europe."
    ),
    _edge(
        "player_neymar_saudi_2023",
        "player_neymar",
        CausalStrength.HIGH,
        "legacy",
        "Neymar's Al Hilal move ends his European chapter without "
        "achieving his UCL dream."
    ),

    # Benzema
    _edge(
        "player_benzema_recalled_2021",
        "national_team_france",
        CausalStrength.HIGH,
        "legacy",
        "Benzema's recall ends a six year exile and immediately strengthens "
        "France's attacking options."
    ),
    _edge(
        "player_benzema_ballondor_2022",
        "player_benzema",
        CausalStrength.HIGH,
        "legacy",
        "Winning the Ballon d'Or at 34 redefines Benzema's career legacy "
        "and his place among the greats."
    ),
    _edge(
        "player_benzema_wc2022_injury",
        "national_team_france",
        CausalStrength.HIGH,
        "legacy",
        "Losing Benzema to injury before the tournament begins removes "
        "France's best attacker from their World Cup campaign."
    ),
    _edge(
        "player_benzema_saudi_2023",
        "club_realmadrid",
        CausalStrength.HIGH,
        "legacy",
        "Benzema's departure closes the Galactico era at Real Madrid "
        "and accelerates Vinicius Jr's ascension."
    ),

    # Lewandowski
    _edge(
        "player_lewandowski_no_ballondor_2020",
        "player_lewandowski",
        CausalStrength.HIGH,
        "legacy",
        "COVID cancellation of the 2020 Ballon d'Or robs Lewandowski "
        "of his most deserved award, a widely acknowledged injustice."
    ),
    _edge(
        "player_lewandowski_barcelona_2022",
        "club_barcelona",
        CausalStrength.HIGH,
        "transfer",
        "Lewandowski's surprise move to Barcelona signals a new era "
        "for the club and his desire for a new challenge at 33."
    ),

    # Kane
    _edge(
        "player_kane_goldboot_2018",
        "player_kane",
        CausalStrength.HIGH,
        "legacy",
        "Winning the 2018 Golden Boot establishes Kane as a world class "
        "striker on the global stage."
    ),
    _edge(
        "player_kane_penalty_miss_2022",
        "player_kane",
        CausalStrength.MEDIUM,
        "legacy",
        "Kane's missed penalty in the 2022 quarterfinal shootout adds "
        "a painful question mark to his international legacy."
    ),
    _edge(
        "player_kane_bayern_2023",
        "player_kane",
        CausalStrength.HIGH,
        "transfer",
        "Kane's Bayern Munich move ends his trophyless Spurs chapter "
        "and gives him his first realistic chance of silverware."
    ),

    # Salah
    _edge(
        "player_salah_ucl_injury_2018",
        "player_salah",
        CausalStrength.HIGH,
        "legacy",
        "Salah's shoulder injury in the 2018 final changes the trajectory "
        "of his peak season and fuels a powerful revenge narrative."
    ),
    _edge(
        "player_salah_contract_2022",
        "club_liverpool",
        CausalStrength.MEDIUM,
        "transfer",
        "Salah's contract extension commits him to Liverpool despite "
        "significant interest from elsewhere."
    ),

    # Vinicius Jr
    _edge(
        "player_vinicius_ucl_final_2022",
        "player_vinicius",
        CausalStrength.HIGH,
        "legacy",
        "Vinicius's UCL final winning goal announces him as the next "
        "great Brazilian and a future Ballon d'Or contender."
    ),
    _edge(
        "player_vinicius_racism_incidents",
        "player_vinicius",
        CausalStrength.HIGH,
        "legacy",
        "Vinicius becomes the face of the anti-racism movement in football, "
        "adding a dimension to his legacy beyond pure football."
    ),

    # Haaland
    _edge(
        "player_haaland_mancity_2022",
        "club_mancity",
        CausalStrength.HIGH,
        "transfer",
        "Haaland's arrival fundamentally changes City's attacking dynamic "
        "and Premier League power balance."
    ),
    _edge(
        "player_haaland_treble_2023",
        "player_haaland",
        CausalStrength.HIGH,
        "legacy",
        "Haaland's treble season with record breaking goal tallies "
        "defines him as the dominant striker of his generation."
    ),

    # Modric
    _edge(
        "player_modric_ballondor_2018",
        "player_modric",
        CausalStrength.HIGH,
        "legacy",
        "Breaking the Messi-Ronaldo Ballon d'Or duopoly after ten years "
        "is one of the most significant individual achievements of the era."
    ),

    # De Bruyne
    _edge(
        "player_debruyne_ucl_final_injury_2021",
        "club_mancity",
        CausalStrength.HIGH,
        "legacy",
        "De Bruyne's early injury in the 2021 UCL final significantly "
        "contributes to City's defeat against Chelsea."
    ),
    _edge(
        "player_debruyne_belgium_legacy",
        "national_team_belgium",
        CausalStrength.HIGH,
        "legacy",
        "De Bruyne's golden generation ends without a major international "
        "trophy despite being one of the best squads in Belgian history."
    ),

    # Pogba
    _edge(
        "player_pogba_post2018_decline",
        "club_manutd",
        CausalStrength.HIGH,
        "legacy",
        "Pogba never replicates his 2018 World Cup form at club level, "
        "his Manchester United career becoming one of football's great "
        "underachievements."
    ),
    _edge(
        "player_pogba_doping_ban_2023",
        "player_pogba",
        CausalStrength.HIGH,
        "legacy",
        "Pogba's four year doping ban effectively ends his career "
        "prematurely after his Juventus return."
    ),

    # Rodri
    _edge(
        "player_rodri_ballondor_2024",
        "player_rodri",
        CausalStrength.HIGH,
        "legacy",
        "Rodri becomes the first defensive midfielder to win the Ballon "
        "d'Or in decades, recognising his unique dominance."
    ),

    # Bellingham
    _edge(
        "player_bellingham_realmadrid_2023",
        "player_bellingham",
        CausalStrength.HIGH,
        "transfer",
        "Bellingham's Real Madrid move is the most anticipated young "
        "player transfer of the era."
    ),
    _edge(
        "player_bellingham_realmadrid_debut",
        "player_bellingham",
        CausalStrength.HIGH,
        "legacy",
        "Bellingham's immediate impact at Real Madrid confirms him as "
        "the most complete young player in world football."
    ),

    # Gvardiol
    _edge(
        "player_gvardiol_wc2022",
        "player_gvardiol",
        CausalStrength.HIGH,
        "legacy",
        "Gvardiol's World Cup performances announce him as the world's "
        "best young defender and trigger his record breaking transfer."
    ),
    _edge(
        "player_gvardiol_mancity_2023",
        "player_gvardiol",
        CausalStrength.MEDIUM,
        "transfer",
        "Gvardiol's slow adaptation at Man City after his record move "
        "shows the difficulty of the Premier League adjustment."
    ),

    # Courtois
    _edge(
        "player_courtois_ucl_final_2022",
        "player_courtois",
        CausalStrength.HIGH,
        "legacy",
        "Courtois's UCL final display is widely considered the greatest "
        "individual goalkeeping performance in final history."
    ),
    _edge(
        "player_courtois_belgium_legacy",
        "national_team_belgium",
        CausalStrength.HIGH,
        "legacy",
        "Courtois never wins a major trophy with Belgium despite being "
        "their greatest ever goalkeeper."
    ),
]


# ---------------------------------------------------------------------------
# Counterfactual - if France wins 2022
# ---------------------------------------------------------------------------

COUNTERFACTUAL_FRANCE_WINS_2022: list[CausalEdge] = [
    _edge(
        "counterfactual_france_wins_2022",
        "player_mbappe",
        CausalStrength.HIGH,
        "legacy",
        "Winning back to back World Cups in 2018 and 2022 puts Mbappe "
        "into the GOAT conversation immediately at age 23."
    ),
    _edge(
        "counterfactual_france_wins_2022",
        "player_messi",
        CausalStrength.HIGH,
        "legacy",
        "Messi does not win the 2022 World Cup, reigniting the GOAT debate "
        "that Argentina's real win had resolved."
    ),
    _edge(
        "counterfactual_france_wins_2022",
        "manager_deschamps",
        CausalStrength.HIGH,
        "legacy",
        "Back to back World Cups fully secures Deschamps legacy, contract "
        "extension is certain and immediate."
    ),
    _edge(
        "counterfactual_france_wins_2022",
        "manager_scaloni",
        CausalStrength.HIGH,
        "legacy",
        "Argentina failing to win 2022 puts Scaloni under immediate pressure "
        "despite the golden generation reaching the final."
    ),
    _edge(
        "counterfactual_france_wins_2022",
        "player_mbappe",
        CausalStrength.MEDIUM,
        "transfer",
        "Back to back World Cup wins give Mbappe stronger negotiating "
        "leverage, Real Madrid likely adjusts terms despite free transfer."
    ),
    _edge(
        "counterfactual_france_wins_2022",
        "player_messi",
        CausalStrength.MEDIUM,
        "legacy",
        "Without the 2022 trophy the cultural weight of the Inter Miami "
        "move is reduced. Messi moves as a great, not the undisputed GOAT."
    ),
    _edge(
        "counterfactual_france_wins_2022",
        "player_messi",
        CausalStrength.MEDIUM,
        "award",
        "Ballon d'Or 2023 is less certain for Messi without the 2022 World "
        "Cup. Mbappe or Haaland have a stronger case."
    ),
    _edge(
        "counterfactual_france_wins_2022",
        "player_dimaria",
        CausalStrength.MEDIUM,
        "legacy",
        "Di Maria retires from international football without a World Cup "
        "winners medal, leaving his legacy incomplete."
    ),
    _edge(
        "counterfactual_france_wins_2022",
        "player_giroud",
        CausalStrength.LOW,
        "legacy",
        "Giroud's all time France top scorer record gains more spotlight "
        "as part of a back to back World Cup winning squad."
    ),
    _edge(
        "counterfactual_france_wins_2022",
        "club_psg",
        CausalStrength.LOW,
        "commercial",
        "Mbappe winning back to back World Cups causes a brief commercial "
        "spike for PSG before his inevitable departure."
    ),
]


# ---------------------------------------------------------------------------
# Counterfactual - if Argentina wins 2018
# ---------------------------------------------------------------------------

COUNTERFACTUAL_ARGENTINA_WINS_2018: list[CausalEdge] = [
    _edge(
        "counterfactual_argentina_wins_2018",
        "player_messi",
        CausalStrength.HIGH,
        "legacy",
        "Messi winning the World Cup in 2018 resolves the GOAT debate "
        "six years earlier, fundamentally changing his remaining career."
    ),
    _edge(
        "counterfactual_argentina_wins_2018",
        "player_mbappe",
        CausalStrength.HIGH,
        "legacy",
        "Mbappe losing the 2018 final in his debut World Cup makes hunger "
        "to win the defining narrative of his early career."
    ),
    _edge(
        "counterfactual_argentina_wins_2018",
        "manager_deschamps",
        CausalStrength.HIGH,
        "legacy",
        "France losing the 2018 final puts Deschamps under immediate "
        "pressure, possible resignation follows."
    ),
    _edge(
        "counterfactual_argentina_wins_2018",
        "player_messi",
        CausalStrength.MEDIUM,
        "legacy",
        "Messi winning in 2018 means he may retire earlier, potentially "
        "before or shortly after the 2022 tournament."
    ),
    _edge(
        "counterfactual_argentina_wins_2018",
        "player_mbappe",
        CausalStrength.MEDIUM,
        "legacy",
        "Losing the 2018 final as a teenager makes the 2022 World Cup "
        "a redemption narrative rather than a coronation."
    ),
    _edge(
        "counterfactual_argentina_wins_2018",
        "player_pogba",
        CausalStrength.MEDIUM,
        "legacy",
        "France losing 2018 means Pogba's peak international moment never "
        "happens, shifting his career trajectory and confidence."
    ),
    _edge(
        "counterfactual_argentina_wins_2018",
        "player_messi",
        CausalStrength.LOW,
        "career",
        "Messi winning in 2018 potentially accelerates the Inter Miami "
        "move timeline as the primary motivation is already achieved."
    ),
    _edge(
        "counterfactual_argentina_wins_2018",
        "national_team_france",
        CausalStrength.LOW,
        "morale",
        "France losing the 2018 final means the golden generation loses "
        "its confidence-defining moment, affecting 2022 preparation."
    ),
]


# ---------------------------------------------------------------------------
# Master registry
# ---------------------------------------------------------------------------

ALL_CAUSAL_EDGES: list[CausalEdge] = (
    REAL_2018_CAUSAL_EDGES
    + REAL_2022_CAUSAL_EDGES
    + REAL_UCL_CAUSAL_EDGES
    + PLAYER_CAUSAL_EDGES
    + COUNTERFACTUAL_FRANCE_WINS_2022
    + COUNTERFACTUAL_ARGENTINA_WINS_2018
)