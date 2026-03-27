# Note stratégique — Marchés publics européens (2009–2017)

## 1. Message exécutif
Le jeu de données met en évidence trois constats utiles pour la décision publique :
- la concurrence est très inégale selon les procédures ;
- l’analyse PME n’est fiable qu’à partir de 2016–2017 en raison d’un fort déficit de reporting avant cette date ;
- le risque budgétaire le plus prioritaire n’est pas le “montant élevé” seul, mais le couple **montant élevé + faible concurrence**.

## 2. KPI recommandés
### Axe A — Concurrence
- **Nombre médian d’offres** : mesure robuste du niveau concurrentiel.
- **Part des marchés à faible concurrence** (`NUMBER_OFFERS <= 2`) : excellent KPI de pilotage.
- **Part des marchés mono-offre** (`NUMBER_OFFERS <= 1`) : KPI d’alerte.

### Axe B — Accès des PME
- **Taux de succès PME observé** (`B_CONTRACTOR_SME = Y`) sur 2016–2017.
- **Taux de couverture du reporting PME** : KPI de qualité de la donnée, indispensable avant tout arbitrage.
- **Taux PME par procédure / critère / secteur**.

### Axe C — Efficience budgétaire
- **Valeur médiane des marchés** par pays / secteur / procédure.
- **Part des marchés de forte valeur et faible concurrence**.
- **Montants exposés au risque concurrentiel** : somme de `AWARD_VALUE_EURO` sur les marchés à faible concurrence.

## 3. Résultats clés à mettre en avant
- La valeur des marchés est **extrêmement asymétrique** : médiane ≈ **46,5 k€**, moyenne ≈ **1,52 M€**. Il faut donc **piloter à la médiane**, pas à la moyenne.
- Environ **51,6 %** des marchés ont **2 offres ou moins**.
- Environ **35,6 %** sont en **mono-offre**.
- Environ **10,6 %** de l’ensemble des marchés cumulent **forte valeur (top 25 %) + faible concurrence**.
- L’indicateur PME est quasi inutilisable avant 2016 : couverture proche de **0 % en 2015**, **28,7 % en 2016**, **73,4 % en 2017**.

## 4. Insights décisionnels
### 4.1 Procédures
Sur les procédures les plus fréquentes, la procédure **restricted (RES)** affiche le meilleur profil concurrentiel parmi les grandes catégories :
- part de faible concurrence ≈ **35,8 %** ;
- nombre médian d’offres ajusté par taille de marché ≈ **4,0**.

À l’inverse, la procédure **negotiated without call (NOC)** concentre le risque :
- part de faible concurrence ≈ **85,2 %** ;
- nombre médian d’offres ≈ **1**.

### 4.2 Critères d’attribution
À taille de marché comparable :
- le critère **MEAT / meilleure offre (M)** a une part de faible concurrence plus basse (**48,4 %**) que le **lowest price (L)** (**53,1 %**) ;
- mais le **lowest price** semble davantage corrélé au succès PME observé. Cela suggère un arbitrage politique entre ouverture concurrentielle et inclusion PME.

### 4.3 Outils de procédure
À taille de marché comparable :
- les **framework agreements** sont associés à une concurrence plus forte (faible concurrence ≈ **35,0 %** contre **55,6 %** hors cadre) ;
- les **dynamic purchasing systems** sont favorables à la fois à la concurrence et aux PME dans les données observées ;
- les **electronic auctions** améliorent la concurrence mais s’accompagnent d’un **taux PME plus faible**, donc à encadrer.

## 5. Recommandations managériales
### Recommandation 1 — Cibler en priorité les gros marchés négociés sans appel
Sur les marchés du **top 25 % en valeur**, les procédures **NOC** représentent environ **26,9 k** contrats. Leur part de faible concurrence atteint **89,9 %**.

**Action** : instaurer une revue ex ante ou un régime de justification renforcée pour les gros marchés en NOC.

**Impact attendu** : si ces marchés convergeaient seulement vers le niveau de risque des procédures ouvertes, cela représenterait environ **13,4 k marchés** sortant de la zone de faible concurrence.

### Recommandation 2 — Faire des procédures open/restricted la référence par défaut
Les procédures **OPE/RES** sont les meilleurs points de comparaison pour le pilotage concurrentiel.

**Action** : créer un indicateur réglementaire “écart à la concurrence de référence” par pays, secteur et acheteur.

### Recommandation 3 — Piloter les PME avec un double objectif “taux PME + qualité de reporting”
Avant d’imposer des quotas ou objectifs, il faut d’abord fiabiliser la donnée.

**Action** : fixer un objectif de **couverture PME > 90 %** avant d’évaluer les administrations sur leur performance PME.

### Recommandation 4 — Utiliser davantage les DPS et les accords-cadres dans les segments adaptés
Dans les données observées, ces instruments ont un profil favorable.

**Action** : lancer des pilotes sectoriels sur 2–3 segments CPV où la concurrence est faible et la standardisation forte.

### Recommandation 5 — Créer une watchlist “forte valeur + faible concurrence”
C’est le meilleur KPI d’efficience budgétaire pour prioriser audit, accompagnement ou réforme.

**Action** : chaque pays devrait suivre mensuellement la part et le montant total des marchés concernés.

## 6. User stories
### Story 1
En tant que **responsable politique européen**,
Je veux **identifier les procédures qui génèrent le plus de marchés à faible concurrence**,
Afin de **prioriser les réformes réglementaires**.

KPI : part de marchés à ≤2 offres, mono-offre, médiane d’offres.

### Story 2
En tant que **pilote PME**, 
Je veux **repérer les critères et outils de passation qui favorisent ou défavorisent les PME**, 
Afin de **concevoir des mesures d’accès ciblées**.

KPI : taux PME, couverture du reporting PME, taux PME par critère/procédure.

### Story 3
En tant que **superviseur budgétaire**, 
Je veux **suivre les marchés de forte valeur passés dans de mauvaises conditions concurrentielles**, 
Afin de **cibler les audits et plans d’amélioration**.

KPI : part des marchés forte valeur + faible concurrence, montants à risque.

## 7. Structure du dashboard
1. **Vue exécutive** : 8 KPI cards.
2. **Concurrence** : évolution temporelle, benchmark procédures, segmentation pays/secteurs.
3. **PME** : couverture de donnée, taux PME, comparaisons ajustées.
4. **Efficience** : matrice de risque pays x secteur, focus “haute valeur / faible concurrence”.
5. **Recommandations** : 4 à 5 actions activables immédiatement.

## 8. Script vidéo (7 min)
- 0:00–0:45 : enjeu macro et question de décision.
- 0:45–1:45 : qualité des données et choix méthodologiques.
- 1:45–3:15 : démonstration Axe A concurrence.
- 3:15–4:30 : démonstration Axe B PME.
- 4:30–5:45 : démonstration Axe C efficience budgétaire.
- 5:45–7:00 : recommandations finales et cas d’usage décideur.
