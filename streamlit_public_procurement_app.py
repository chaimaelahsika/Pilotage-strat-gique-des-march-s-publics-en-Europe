import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Marchés publics UE",
    layout="wide"
)

# =========================
# STYLE
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Fond global */
.stApp {
    background: linear-gradient(180deg, #081625 0%, #0B1F33 100%);
    color: #EAF2FF;
}

/* Titres */
h1, h2, h3 {
    color: #EAF2FF !important;
    font-weight: 700 !important;
}

h4, h5, h6, p, label, span {
    color: #D8E6F7;
}

/* Caption */
div[data-testid="stCaptionContainer"] {
    color: #AFC3DA !important;
    font-size: 1rem !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #06111D !important;
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* KPI cards */
div[data-testid="metric-container"] {
    background: linear-gradient(180deg, #F8FBFF 0%, #EEF5FC 100%);
    border: 1px solid #D7E3F1;
    border-left: 6px solid #3B82F6;
    padding: 18px 20px;
    border-radius: 18px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.18);
}
<div style="
    background: linear-gradient(135deg, #163B65 0%, #1F5A99 100%);
    padding: 28px 32px;
    border-radius: 22px;
    margin-bottom: 24px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.22);
    border: 1px solid rgba(255,255,255,0.08);
">
    <div style="color: white; font-size: 2rem; font-weight: 800; margin-bottom: 6px;">
        Pilotage stratégique des marchés publics en Europe
    </div>
    <div style="color: #DCEBFA; font-size: 1rem;">
        DG GROW — concurrence, accès des PME et efficience budgétaire
    </div>
</div>
<div style="
    background: linear-gradient(90deg, #12385C 0%, #1E4E79 100%);
    padding: 10px 16px;
    border-radius: 14px;
    margin-bottom: 12px;
    color: white;
    font-weight: 700;
">
    Concurrence et risque
</div>

div[data-testid="metric-container"] label {
    color: #5B6B82 !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
}

div[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #0E2A47 !important;
    font-weight: 800 !important;
    font-size: 2.2rem !important;
}

/* Onglets */
button[data-baseweb="tab"] {
    background: #16324D !important;
    color: #DDE9F8 !important;
    border-radius: 12px 12px 0 0 !important;
    padding: 10px 18px !important;
    font-weight: 700 !important;
    border: none !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    background: #2A6FBB !important;
    color: white !important;
}

/* Tableaux */
div[data-testid="stDataFrame"] {
    background: white;
    border-radius: 16px;
    padding: 8px;
    border: 1px solid #D9E2EC;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.14);
}

/* Alertes */
div[data-testid="stInfo"] {
    background-color: #102941 !important;
    border: 1px solid #2D5B87 !important;
    color: #EAF2FF !important;
    border-radius: 14px !important;
}

div[data-testid="stSuccess"] {
    background-color: #0E2D21 !important;
    border: 1px solid #2F7D5A !important;
    color: #EAFBF1 !important;
    border-radius: 14px !important;
}

div[data-testid="stWarning"] {
    background-color: #3B2412 !important;
    border: 1px solid #A8642A !important;
    color: #FFF2E8 !important;
    border-radius: 14px !important;
}

/* Séparateur */
hr {
    border-top: 1px solid rgba(255,255,255,0.12) !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div style="background: linear-gradient(135deg, #163B65 0%, #1F5A99 100%);
            padding: 26px 30px;
            border-radius: 20px;
            margin-bottom: 18px;
            box-shadow: 0 8px 24px rgba(22,59,101,0.18);">
    <div style="color: white; font-size: 2rem; font-weight: 800; margin-bottom: 6px;">
        Pilotage stratégique des marchés publics en Europe
    </div>
    <div style="color: #EAF4FF; font-size: 1rem;">
        DG GROW — concurrence, accès des PME et efficience budgétaire
    </div>
</div>
""", unsafe_allow_html=True)

CSV_PATH = "/Users/chaimaelahsika/Documents/Desktop/Projet BI/dataChallenge_training.csv"

TOP_TYPE_LABELS = {
    "OPE": "Procédure ouverte",
    "RES": "Procédure restreinte",
    "NIC": "Procédure négociée avec appel",
    "NOC": "Procédure négociée sans appel",
    "AWP": "Attribution sans publication préalable",
    "COD": "Dialogue compétitif",
    "NOP": "Non spécifié / autre NOP",
    "NIP": "Non spécifié / autre NIP",
    "INP": "Innovation / autre INP"
}

CRIT_LABELS = {
    "L": "Prix le plus bas",
    "M": "Offre économiquement la plus avantageuse"
}

CONTRACT_LABELS = {
    "W": "Travaux",
    "S": "Services",
    "U": "Fournitures"
}

COUNTRY_LABELS = {
    "AT": "Autriche",
    "BE": "Belgique",
    "BG": "Bulgarie",
    "CY": "Chypre",
    "CZ": "Tchéquie",
    "DE": "Allemagne",
    "DK": "Danemark",
    "EE": "Estonie",
    "ES": "Espagne",
    "FI": "Finlande",
    "FR": "France",
    "HR": "Croatie",
    "HU": "Hongrie",
    "IE": "Irlande",
    "IT": "Italie",
    "LT": "Lituanie",
    "LU": "Luxembourg",
    "EL": "Grèce",
    "GR": "Grèce",
    "LV": "Lettonie",
    "MT": "Malte",
    "NL": "Pays-Bas",
    "PL": "Pologne",
    "PT": "Portugal",
    "RO": "Roumanie",
    "SE": "Suède",
    "SI": "Slovénie",
    "SK": "Slovaquie",
    "UK": "Royaume-Uni",
    "CH": "Suisse",
    "IS": "Islande",
    "LI": "Liechtenstein",
    "NO": "Norvège",
    "MK": "Macédoine du Nord"
}


def build_cleaning_log(step, before_n, after_n, comment):
    return {
        "Étape": step,
        "Lignes avant": int(before_n),
        "Lignes après": int(after_n),
        "Lignes retirées": int(before_n - after_n),
        "Commentaire": comment
    }


def winsorize_series(s: pd.Series, lower_q=0.01, upper_q=0.99):
    low = s.quantile(lower_q)
    high = s.quantile(upper_q)
    return s.clip(lower=low, upper=high), low, high


def fmt_pct(x):
    return f"{x:.1%}" if pd.notna(x) else "NA"


def fmt_int(x):
    return f"{int(x):,}".replace(",", " ") if pd.notna(x) else "NA"


def fmt_eur(x):
    return f"{x:,.0f} €".replace(",", " ") if pd.notna(x) else "NA"


def weighted_group_compare(df: pd.DataFrame, column: str) -> pd.DataFrame:
    tmp = df.dropna(subset=[column, "AWARD_VALUE_EURO_WINS"]).copy()

    if tmp.empty:
        return pd.DataFrame(columns=[
            column,
            "Nombre de marchés",
            "Part de faible concurrence",
            "Médiane d'offres (ajustée valeur)",
            "Taux de succès PME"
        ])

    tmp["value_band"] = pd.qcut(tmp["AWARD_VALUE_EURO_WINS"], q=10, duplicates="drop")

    grouped = (
        tmp.groupby(["value_band", column], observed=False)
        .agg(
            n=("ID_AW", "size"),
            low_comp_share=("low_comp", "mean"),
            median_offers=("NUMBER_OFFERS", "median"),
            sme_rate=("sme_flag", "mean")
        )
        .reset_index()
    )

    rows = []
    for label, g in grouped.groupby(column, observed=False):
        weights = g["n"].fillna(0).astype(float)
        if weights.sum() == 0:
            continue

        rows.append({
            column: label,
            "Nombre de marchés": int(g["n"].sum()),
            "Part de faible concurrence": np.average(g["low_comp_share"].fillna(0), weights=weights),
            "Médiane d'offres (ajustée valeur)": np.average(g["median_offers"].fillna(0), weights=weights),
            "Taux de succès PME": np.average(g["sme_rate"].fillna(0), weights=weights)
        })

    return pd.DataFrame(rows).sort_values("Part de faible concurrence", ascending=True)


@st.cache_data(show_spinner=True)
def load_and_clean_data(path: str):
    logs = []

    df = pd.read_csv(path)
    n0 = len(df)
    logs.append(build_cleaning_log("Chargement initial", n0, n0, "Lecture brute du fichier CSV."))

    before = len(df)
    df = df.drop_duplicates(subset=["ID_AW"]).copy()
    after = len(df)
    logs.append(build_cleaning_log(
        "Suppression des doublons sur ID_AW", before, after,
        "Conservation d'une seule ligne par identifiant de marché."
    ))

    str_cols = [
        "ISO_COUNTRY_CODE", "TYPE_OF_CONTRACT", "TOP_TYPE", "CPV",
        "B_ELECTRONIC_AUCTION", "B_DYN_PURCH_SYST", "B_FRA_AGREEMENT",
        "B_GPA", "B_ON_BEHALF", "B_SUBCONTRACTED", "CRIT_CODE",
        "B_CONTRACTOR_SME"
    ]
    for col in str_cols:
        if col in df.columns:
            df[col] = df[col].astype("string").str.strip().str.upper()

    if "MAIN_ACTIVITY" in df.columns:
        df["MAIN_ACTIVITY"] = df["MAIN_ACTIVITY"].astype("string").str.strip()

    num_cols = [
        "ID_AW", "LOTS_NUMBER", "YEAR", "CAE_TYPE", "CRIT_PRICE_WEIGHT",
        "NUMBER_AWARDS", "NUMBER_OFFERS", "AWARD_VALUE_EURO"
    ]
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    before = len(df)
    df = df[df["YEAR"].between(2009, 2017, inclusive="both")].copy()
    after = len(df)
    logs.append(build_cleaning_log(
        "Filtrage période 2009–2017",
        before,
        after,
        "Exclusion des lignes hors périmètre d'étude."
    ))

    before = len(df)
    df = df.dropna(subset=["ID_AW", "YEAR", "ISO_COUNTRY_CODE"]).copy()
    after = len(df)
    logs.append(build_cleaning_log(
        "Suppression des lignes sans identifiant/année/pays",
        before,
        after,
        "Ces variables sont indispensables aux analyses."
    ))

    before = len(df)
    neg_count = int((df["AWARD_VALUE_EURO"] < 0).sum(skipna=True))
    df = df[(df["AWARD_VALUE_EURO"].isna()) | (df["AWARD_VALUE_EURO"] >= 0)].copy()
    after = len(df)
    logs.append(build_cleaning_log(
        "Suppression des montants négatifs",
        before,
        after,
        f"Retrait des lignes avec AWARD_VALUE_EURO < 0 ({neg_count} lignes)."
    ))

    before = len(df)
    neg_offers = int((df["NUMBER_OFFERS"] < 0).sum(skipna=True))
    df = df[(df["NUMBER_OFFERS"].isna()) | (df["NUMBER_OFFERS"] >= 0)].copy()
    after = len(df)
    logs.append(build_cleaning_log(
        "Suppression des nombres d'offres négatifs",
        before,
        after,
        f"Retrait des lignes avec NUMBER_OFFERS < 0 ({neg_offers} lignes)."
    ))

    before = len(df)
    neg_awards = int((df["NUMBER_AWARDS"] < 0).sum(skipna=True))
    df = df[(df["NUMBER_AWARDS"].isna()) | (df["NUMBER_AWARDS"] >= 0)].copy()
    after = len(df)
    logs.append(build_cleaning_log(
        "Suppression des nombres d'attributions négatifs",
        before,
        after,
        f"Retrait des lignes avec NUMBER_AWARDS < 0 ({neg_awards} lignes)."
    ))

    valid_contracts = {"W", "S", "U"}
    valid_crit = {"L", "M"}
    valid_binary = {"Y", "N"}

    if "TYPE_OF_CONTRACT" in df.columns:
        df["TYPE_OF_CONTRACT"] = df["TYPE_OF_CONTRACT"].where(df["TYPE_OF_CONTRACT"].isin(valid_contracts))
    if "CRIT_CODE" in df.columns:
        df["CRIT_CODE"] = df["CRIT_CODE"].where(df["CRIT_CODE"].isin(valid_crit))

    for col in [
        "B_ELECTRONIC_AUCTION", "B_DYN_PURCH_SYST", "B_FRA_AGREEMENT",
        "B_GPA", "B_ON_BEHALF", "B_SUBCONTRACTED", "B_CONTRACTOR_SME"
    ]:
        if col in df.columns:
            df[col] = df[col].where(df[col].isin(valid_binary))

    df["CPV2"] = df["CPV"].astype("string").str.extract(r"CPV(\d{2})", expand=False)
    df["sme_flag"] = df["B_CONTRACTOR_SME"].map({"Y": 1, "N": 0})
    df["low_comp"] = np.where(df["NUMBER_OFFERS"].notna(), df["NUMBER_OFFERS"] <= 2, np.nan)
    df["single_bid"] = np.where(df["NUMBER_OFFERS"].notna(), df["NUMBER_OFFERS"] <= 1, np.nan)

    df["top_type_label"] = df["TOP_TYPE"].map(TOP_TYPE_LABELS).fillna(df["TOP_TYPE"])
    df["crit_label"] = df["CRIT_CODE"].map(CRIT_LABELS).fillna(df["CRIT_CODE"])
    df["contract_label"] = df["TYPE_OF_CONTRACT"].map(CONTRACT_LABELS).fillna(df["TYPE_OF_CONTRACT"])
    df["pays_nom"] = df["ISO_COUNTRY_CODE"].map(COUNTRY_LABELS).fillna(df["ISO_COUNTRY_CODE"])

    df["award_value_valid"] = df["AWARD_VALUE_EURO"].notna() & (df["AWARD_VALUE_EURO"] > 0)
    df["AWARD_VALUE_EURO_WINS"] = np.nan
    df["award_outlier_low"] = False
    df["award_outlier_high"] = False
    df["award_log"] = np.nan

    positive_awards = df.loc[df["award_value_valid"], "AWARD_VALUE_EURO"]
    if len(positive_awards) > 0:
        wins, low_w, high_w = winsorize_series(positive_awards, lower_q=0.01, upper_q=0.99)
        df.loc[df["award_value_valid"], "AWARD_VALUE_EURO_WINS"] = wins.values
        df.loc[df["award_value_valid"], "award_outlier_low"] = df.loc[df["award_value_valid"], "AWARD_VALUE_EURO"] < low_w
        df.loc[df["award_value_valid"], "award_outlier_high"] = df.loc[df["award_value_valid"], "AWARD_VALUE_EURO"] > high_w
        df.loc[df["award_value_valid"], "award_log"] = np.log1p(
            df.loc[df["award_value_valid"], "AWARD_VALUE_EURO_WINS"]
        )

    coverage_by_year = (
        df.groupby("YEAR")["sme_flag"]
        .apply(lambda x: x.notna().mean())
        .reset_index(name="couverture_pme")
    )

    df = df.merge(coverage_by_year, on="YEAR", how="left")
    df["analyse_pme_fiable"] = df["couverture_pme"] >= 0.5

    quality_summary = pd.DataFrame({
        "Indicateur": [
            "Nombre de lignes final",
            "Part AWARD_VALUE_EURO manquant ou <= 0",
            "Part NUMBER_OFFERS manquant",
            "Part SME manquant"
        ],
        "Valeur": [
            len(df),
            (1 - df["award_value_valid"].mean()) if len(df) else np.nan,
            df["NUMBER_OFFERS"].isna().mean() if len(df) else np.nan,
            df["sme_flag"].isna().mean() if len(df) else np.nan
        ]
    })

    cleaning_log = pd.DataFrame(logs)
    return df, cleaning_log, quality_summary, coverage_by_year


df, cleaning_log, quality_summary, coverage_by_year = load_and_clean_data(CSV_PATH)

with st.sidebar:
    st.header("Filtres")

    years = st.multiselect(
        "Années",
        sorted(df["YEAR"].dropna().unique()),
        default=sorted(df["YEAR"].dropna().unique())
    )
    countries = st.multiselect(
        "Pays",
        sorted(df["pays_nom"].dropna().unique()),
        default=[]
    )
    contracts = st.multiselect(
        "Type de contrat",
        sorted(df["contract_label"].dropna().unique()),
        default=[]
    )
    procedures = st.multiselect(
        "Procédure",
        sorted(df["top_type_label"].dropna().unique()),
        default=[]
    )
    crits = st.multiselect(
        "Critère d'attribution",
        sorted(df["crit_label"].dropna().unique()),
        default=[]
    )
    cpv2 = st.multiselect(
        "CPV à 2 chiffres",
        sorted(df["CPV2"].dropna().unique()),
        default=[]
    )

    valid_values = df.loc[df["award_value_valid"], "AWARD_VALUE_EURO_WINS"].dropna()
    if len(valid_values) > 0:
        min_value = float(valid_values.min())
        max_value = float(valid_values.max())
        value_range = st.slider(
            "Plage de valeur des marchés",
            min_value=min_value,
            max_value=max_value,
            value=(min_value, max_value)
        )
    else:
        value_range = (0.0, 0.0)

f = df[df["YEAR"].isin(years)].copy()

if countries:
    f = f[f["pays_nom"].isin(countries)]
if contracts:
    f = f[f["contract_label"].isin(contracts)]
if procedures:
    f = f[f["top_type_label"].isin(procedures)]
if crits:
    f = f[f["crit_label"].isin(crits)]
if cpv2:
    f = f[f["CPV2"].isin(cpv2)]

if len(valid_values) > 0:
    f = f[
        (f["AWARD_VALUE_EURO_WINS"].isna()) |
        (
            (f["AWARD_VALUE_EURO_WINS"] >= value_range[0]) &
            (f["AWARD_VALUE_EURO_WINS"] <= value_range[1])
        )
    ].copy()

valid_budget = f["AWARD_VALUE_EURO_WINS"].notna()
if valid_budget.any():
    q75 = f.loc[valid_budget, "AWARD_VALUE_EURO_WINS"].quantile(0.75)
    f["high_value_low_comp"] = np.where(
        valid_budget & pd.Series(f["low_comp"]).fillna(False),
        f["AWARD_VALUE_EURO_WINS"] >= q75,
        np.nan
    )
else:
    f["high_value_low_comp"] = np.nan

# =========================
# KPI
# =========================
st.markdown("### Indicateurs clés")

st.markdown("#### Concurrence et risque")
k1, k2, k3 = st.columns(3)
k1.metric("Part de faible concurrence", fmt_pct(pd.Series(f["low_comp"]).mean()))
k2.metric("Part forte valeur & faible concurrence", fmt_pct(pd.Series(f["high_value_low_comp"]).mean()))
k3.metric("Part de mono-offre", fmt_pct(pd.Series(f["single_bid"]).mean()))

st.markdown("#### Budget et PME")
empty1, k4, k5, empty2 = st.columns([0.5, 1, 1, 0.5])
k4.metric(
    "Valeur médiane des marchés",
    fmt_eur(f.loc[f["AWARD_VALUE_EURO_WINS"].notna(), "AWARD_VALUE_EURO_WINS"].median())
)
k5.metric("Taux de succès PME observé", fmt_pct(f["sme_flag"].mean()))

st.markdown("---")

# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "A. Concurrence",
    "B. Accès des PME",
    "C. Efficience budgétaire",
    "Recommandations"
])

with tab1:
    st.subheader("Dynamique concurrentielle")

    annual = (
        f.groupby("YEAR")
        .agg(
            median_offers=("NUMBER_OFFERS", "median"),
            low_comp_share=("low_comp", "mean"),
            single_bid_share=("single_bid", "mean")
        )
        .reset_index()
    )

    if not annual.empty:
        annual_chart = annual.copy()
        annual_chart["YEAR"] = annual_chart["YEAR"].astype(int).astype(str)

        st.markdown("#### Évolution du nombre médian d'offres")
        st.line_chart(annual_chart.set_index("YEAR")[["median_offers"]])

        st.markdown("#### Évolution de la faible concurrence et de la mono-offre")
        st.line_chart(annual_chart.set_index("YEAR")[["low_comp_share", "single_bid_share"]])

    st.markdown("#### Comparaison des procédures")
    proc = (
        f.groupby("top_type_label")
        .agg(
            **{
                "Nombre de marchés": ("ID_AW", "size"),
                "Médiane d'offres": ("NUMBER_OFFERS", "median"),
                "Part de faible concurrence": ("low_comp", "mean"),
                "Valeur médiane": ("AWARD_VALUE_EURO_WINS", "median")
            }
        )
        .sort_values("Part de faible concurrence")
    )

    if not proc.empty:
        proc_display = proc.copy().reset_index().rename(columns={"top_type_label": "Procédure"})
        proc_display["Part de faible concurrence"] = proc_display["Part de faible concurrence"].map(fmt_pct)
        proc_display["Valeur médiane"] = proc_display["Valeur médiane"].map(fmt_eur)
        st.dataframe(proc_display, width="stretch", hide_index=True)

    compare_proc = weighted_group_compare(
        f[f["TOP_TYPE"].isin(["OPE", "RES", "NIC", "NOC", "AWP"])],
        "top_type_label"
    )

    st.caption("Comparaison des procédures ajustée par tranche de valeur des marchés.")
    if not compare_proc.empty:
        compare_proc_display = compare_proc.copy().rename(columns={"top_type_label": "Procédure"})
        compare_proc_display["Part de faible concurrence"] = compare_proc_display["Part de faible concurrence"].map(fmt_pct)
        compare_proc_display["Taux de succès PME"] = compare_proc_display["Taux de succès PME"].map(fmt_pct)
        compare_proc_display["Médiane d'offres (ajustée valeur)"] = compare_proc_display["Médiane d'offres (ajustée valeur)"].round(2)
        st.dataframe(compare_proc_display, width="stretch", hide_index=True)

with tab2:
    st.subheader("Accès des PME")
    st.info("Les analyses PME doivent être interprétées avec prudence avant 2016, car la couverture de reporting est faible.")

    cov = coverage_by_year.copy().rename(columns={"couverture_pme": "Couverture PME"})
    if not cov.empty:
        cov_chart = cov.copy()
        cov_chart["YEAR"] = cov_chart["YEAR"].astype(int).astype(str)
        st.markdown("#### Couverture du reporting PME")
        st.line_chart(cov_chart.set_index("YEAR")[["Couverture PME"]])

    sme_df = f[f["analyse_pme_fiable"] == True].copy()

    if len(sme_df) > 0:
        st.caption("Analyse restreinte aux années où la couverture PME est jugée suffisante.")

        crit = weighted_group_compare(
            sme_df[sme_df["CRIT_CODE"].isin(["L", "M"])],
            "crit_label"
        )
        st.caption("Comparaison des critères d'attribution ajustée par tranche de valeur.")
        if not crit.empty:
            crit_display = crit.copy().rename(columns={"crit_label": "Critère"})
            crit_display["Part de faible concurrence"] = crit_display["Part de faible concurrence"].map(fmt_pct)
            crit_display["Taux de succès PME"] = crit_display["Taux de succès PME"].map(fmt_pct)
            crit_display["Médiane d'offres (ajustée valeur)"] = crit_display["Médiane d'offres (ajustée valeur)"].round(2)
            st.dataframe(crit_display, width="stretch", hide_index=True)

        other = []
        feature_labels = {
            "B_DYN_PURCH_SYST": "Système d'acquisition dynamique",
            "B_ELECTRONIC_AUCTION": "Enchère électronique",
            "B_FRA_AGREEMENT": "Accord-cadre"
        }

        for col in ["B_DYN_PURCH_SYST", "B_ELECTRONIC_AUCTION", "B_FRA_AGREEMENT"]:
            tmp = weighted_group_compare(sme_df[sme_df[col].isin(["Y", "N"])], col)
            if not tmp.empty:
                tmp[col] = tmp[col].map({"Y": "Oui", "N": "Non"})
                tmp = tmp.rename(columns={col: "Modalité"})
                tmp.insert(0, "Levier", feature_labels[col])
                other.append(tmp)

        if other:
            other_df = pd.concat(other, ignore_index=True)
            other_df["Part de faible concurrence"] = other_df["Part de faible concurrence"].map(fmt_pct)
            other_df["Taux de succès PME"] = other_df["Taux de succès PME"].map(fmt_pct)
            other_df["Médiane d'offres (ajustée valeur)"] = other_df["Médiane d'offres (ajustée valeur)"].round(2)
            st.dataframe(other_df, width="stretch", hide_index=True)
    else:
        st.warning("Aucune année avec couverture PME suffisante dans le filtre sélectionné.")

with tab3:
    st.subheader("Radar de risque – efficience budgétaire")

    risk = (
        f.groupby("pays_nom")
        .agg(
            **{
                "Nombre de marchés": ("ID_AW", "size"),
                "Valeur médiane": ("AWARD_VALUE_EURO_WINS", "median"),
                "Part de faible concurrence": ("low_comp", "mean"),
                "Part forte valeur & faible concurrence": ("high_value_low_comp", "mean")
            }
        )
        .query("`Nombre de marchés` >= 5000")
        .sort_values("Part forte valeur & faible concurrence", ascending=False)
    )

    if not risk.empty:
        risk_display = risk.copy().reset_index().rename(columns={"pays_nom": "Pays"})
        risk_display["Valeur médiane"] = risk_display["Valeur médiane"].map(fmt_eur)
        risk_display["Part de faible concurrence"] = risk_display["Part de faible concurrence"].map(fmt_pct)
        risk_display["Part forte valeur & faible concurrence"] = risk_display["Part forte valeur & faible concurrence"].map(fmt_pct)
        st.dataframe(risk_display, width="stretch", hide_index=True)

    sector = (
        f.groupby("CPV2")
        .agg(
            **{
                "Nombre de marchés": ("ID_AW", "size"),
                "Valeur médiane": ("AWARD_VALUE_EURO_WINS", "median"),
                "Part de faible concurrence": ("low_comp", "mean")
            }
        )
        .query("`Nombre de marchés` >= 10000")
        .sort_values("Part de faible concurrence", ascending=False)
    )

    if not sector.empty:
        sector_display = sector.copy().reset_index().rename(columns={"CPV2": "CPV 2 chiffres"})
        sector_display["Valeur médiane"] = sector_display["Valeur médiane"].map(fmt_eur)
        sector_display["Part de faible concurrence"] = sector_display["Part de faible concurrence"].map(fmt_pct)
        st.dataframe(sector_display, width="stretch", hide_index=True)

with tab4:
    st.subheader("Recommandations stratégiques")

    st.markdown("""
Nos recommandations clés : 

\n À partir de cette analyse, nous formulons trois recommandations prioritaires.
\n Recommandations managériales : 
\n- Trois axes d’amélioration se dégagent naturellement.
\n- Le premier consiste à renforcer la concurrence en privilégiant les procédures ouvertes lorsque possible, en encadrant davantage les procédures négociées et en instaurant un examen obligatoire pour les marchés de forte valeur n’ayant attiré qu’une ou deux offres.
\n- Le deuxième vise à accroître la participation des PME grâce à une harmonisation du reporting, une simplification administrative et un découpage stratégique des lots. Ce type de segmentation offre une opportunité concrète d’élargir le champ des entreprises éligibles et ainsi éviter les monopoles dans les marchés publics. 
\n- Le troisième axe consiste à sécuriser les marchés de forte valeur en instaurant un suivi spécifique, notamment par des comparaisons de prix inter‑pays et une obligation de justification renforcée en cas de faible concurrence afin de mieux encadrer les offres.""")

    st.success(
        "Ce tableau de bord sert à orienter les décisions publiques. "
        "Il met en évidence les zones où lancer des audits, des pilotes et des ajustements réglementaires."
    )