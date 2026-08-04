# Nestlé Distributed Order Management — Planner View

**What this is:** a one-page summary of what changes if customer orders are matched to the best available plant, instead of always going through their originally recorded plant — written for a planner or operations manager, not a technical audience.

---

## The situation today

Right now, every order is evaluated against **one specific plant** — wherever it happened to be recorded. If that plant doesn't have enough stock, the order is turned away, even if another plant carries the same product with stock to spare.

Looking at the current order book: **only about 15% of plant capacity is being used**, and a real check found at least one case where a plant was already committed to more orders than it actually has stock for — a 199-unit shortfall waiting to cause a problem.

## What changes when orders can be redirected

We tested letting the system consider **every plant that actually carries the product**, not just the one an order happened to land at, and pick whichever real option is available. Two ways of doing this were compared against doing nothing differently (the "Baseline"):

| | Revenue | Shipping Cost | Orders Redirected | Fill Rate |
|---|---:|---:|---:|---:|
| **Today's process** (no redirecting) | $87.70M | $61.35M | 0 | 98.92% |
| **Simple redirect rule** (try the obvious next-best plant) | $88.09M | $61.67M | 162 | 99.54% |
| **Fully optimized redirect** (best possible combination) | $88.09M | **$53.81M** | 18,899 | 99.54% |

*(Figures are on the full order book — roughly 25,000 order-lines — solved in under 8 seconds.)*

## The bottom line

- **Revenue barely needs to change** to fix this — the current process is already accepting nearly all the orders that make business sense. The opportunity isn't "sell more," it's "ship smarter."
- **Shipping cost is where the real money is.** Fully optimizing which plant fulfills which order cuts shipping spend by **$7.5 million**, without giving up any revenue or fill rate, just by sending orders to cheaper-to-ship-from plants that already carry the same product.
- **A simple version of this gets most of the fill-rate benefit with very little disruption** — the "simple redirect rule" only moves 162 orders and still lifts fill rate to 99.54%. This is a realistic first step if a full system change feels too disruptive to roll out at once.

## One trade-off worth knowing about

Chasing the lowest shipping cost this aggressively means volume concentrates into whichever plants are cheapest to ship from — warehouse utilization actually becomes **less even** across the network (down from a fairly balanced ~92% to a more concentrated ~73%) even though total cost goes down. That's a real trade-off, not a flaw in the analysis: **cutting cost and balancing warehouse load are two different goals**, and optimizing hard for one can pull against the other. A planner may want a version that caps how much volume any one plant can absorb, to keep the network more balanced — the same tools used here can produce that version too.

## Recommended next step

Start with the **simple redirect rule** — it's a small, low-risk change (162 orders) that already closes most of the fill-rate gap. Use the fully optimized version as the target to work toward once the team is comfortable with orders routinely being redirected across plants.
