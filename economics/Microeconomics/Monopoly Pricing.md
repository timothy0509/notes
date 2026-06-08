---
tags:
  - economics
  - microeconomics
  - monopoly
  - pricing
  - elective
---

# Monopoly Pricing

## Simple Monopoly Pricing

Under **simple monopoly pricing**, the monopolist charges the **same price** to all consumers for all units sold (uniform pricing).

### Determination of Price and Output

The monopolist maximises profit where:

$$ MR = MC $$

> [!important] Unlike a perfectly competitive firm ($P = MR$), a monopolist faces a **downward-sloping demand curve**. To sell more, it must lower the price on **all** units, so $MR < P$.

### Step-by-Step: Finding the Monopoly Outcome

1. Derive $MR$ from the demand curve $P = a - bQ$:
   $$ TR = P \times Q = aQ - bQ^2 $$
   $$ MR = \frac{dTR}{dQ} = a - 2bQ $$
   (MR has twice the slope of demand)

2. Set $MR = MC$ to find the profit-maximising quantity $Q_m$

3. Read the price $P_m$ from the **demand curve** at $Q_m$

4. Profit = $(P_m - AC) \times Q_m$

### Graphical Illustration

```
     Price
       │
       │    MC
       │   /
  P_m ─┤  /│
       │ / │
       │/  │
       │   │
  P_c ─┤   ├── D = AR
       │   │
       └───┴──────── Q
          MR   Q_m   Q_c
```

- Competitive outcome (if this were a competitive market): $P_c$, $Q_c$ where $D = MC$
- Monopoly outcome: $P_m > MC$, $Q_m < Q_c$

> [!warning] The monopolist **restricts output** to raise price, creating a **deadweight loss** (allocative inefficiency).

### Efficiency Implications

| Aspect | Monopoly Outcome | Compared to Perfect Competition |
|---|---|---|
| Price | $P_m > MC$ | Higher |
| Quantity | $Q_m < Q_c$ | Lower |
| Consumer surplus | Smaller | Less |
| Producer surplus | Larger | More |
| **Total surplus** | **Smaller** (DWL) | **Reduced** |
| Allocative efficiency? | **No** ($P \ne MC$) | No |
| Productive efficiency? | Not guaranteed | Not guaranteed |

> [!note] The **deadweight loss** from monopoly is the triangular area between $Q_m$ and $Q_c$, bounded by $D$ (willingness to pay) and $MC$ (cost).

### Numerical Example

> [!example] Demand: $P = 100 - 2Q$, $MC = 20$ (constant).
> 
> $MR = 100 - 4Q$  
> Set $MR = MC$: $100 - 4Q = 20 \to Q_m = 20$  
> $P_m = 100 - 2(20) = 60$  
> Profit = $(60 - 20) \times 20 = 800$  
> Competitive output: $P = MC \to 100 - 2Q = 20 \to Q_c = 40$, $P_c = 20$  
> DWL = $\frac{1}{2} \times (40 - 20) \times (60 - 20) = 400$

---

## Price Discrimination

**Price discrimination** occurs when the firm sells the same product to different consumers at **different prices** for reasons **not** related to cost differences.

### Conditions for Price Discrimination

1. **Market power** — the firm must be a price searcher (downward-sloping demand)
2. **Separable markets** — the firm must be able to identify distinct groups with different price elasticities
3. **No resale** — arbitrage must be prevented (otherwise low-price buyers resell to high-price buyers)

> [!info] A perfectly competitive firm **cannot** price discriminate because it is a price taker.

### Types of Price Discrimination

#### First Degree (Perfect Price Discrimination)

The monopolist charges **each consumer** their **maximum willingness to pay**.

- The firm captures **all** consumer surplus
- Output is $Q_c$ (same as competitive output!)
- **No deadweight loss** — but the distribution is extremely unequal (all surplus goes to the firm)
- Rare in practice (requires perfect information about every buyer's willingness to pay)

> [!example] A car dealer negotiating individually with each customer — charging different prices based on perceived willingness to pay.

#### Second Degree (Block Pricing / Non-linear Pricing)

The monopolist charges **different prices for different quantities** or quality tiers.

- Consumers **self-select** into different price brackets
- Common forms: bulk discounts, quantity discounts, versioning

> [!example] **Electricity pricing**: $0.80/kWh for the first 200 units, $0.60/kWh for the next 200 units, $0.40/kWh beyond that. Or: movie theatres charging different prices for adults, children, and seniors.

#### Third Degree (Market Segmentation)

The monopolist charges **different prices in different sub-markets** based on observable characteristics (e.g. age, location, student status).

- Separate the market into segments with **different price elasticities of demand**
- Charge a **higher price** in the less elastic (more inelastic) market
- Charge a **lower price** in the more elastic market

> [!tip] **Rule for third-degree discrimination**: $MR_1 = MR_2 = MC$. Allocate output so that the last unit in each market yields the same marginal revenue.

### Conditions for Each Type

| Type | Name | Condition | Resale | Info Required |
|---|---|---|---|---|
| 1st | Perfect | Charge each buyer their willingness to pay | Impossible | Perfect — know each buyer's demand |
| 2nd | Block pricing / Versioning | Self-selection by quantity/quality tier | Impossible | Moderate — know distribution of types |
| 3rd | Market segmentation | Separate groups by observable trait | Must prevent resale across groups | Low — only need group elasticities |

> [!important] **HKDSE exam tip**: always check the **three conditions** first. If any is missing, price discrimination is impossible.

### Efficiency Implications of Price Discrimination

| Type | Output | DWL | Surplus Distribution |
|---|---|---|---|
| 1st degree | $Q_c$ (efficient) | None | All surplus → producer |
| 2nd degree | Between $Q_m$ and $Q_c$ | Some DWL | Mixed |
| 3rd degree | Ambiguous (could be higher or lower than simple monopoly) | DWL exists | Mixed |

> [!warning] While first-degree price discrimination achieves allocative efficiency ($Q = Q_c$), it raises **equity concerns** — consumers receive no surplus.

---

## Related Topics

- [[Competition and Market Structure]]
- [[Anti-competitive Behaviours and Competition Policy]]
- [[Efficiency, Equity and the Role of Government]]
- [[Market and Price]]
- [[Economics Index]]
