---
title: Period-End Adjustments
date: 2026-06-16
tags:
  - bafs
  - elective
  - financial-accounting
  - adjustments
aliases:
  - Accruals
  - Depreciation
  - Inventory Valuation
  - Bad Debts
---

# Period-End Adjustments

> [!abstract] Overview
> Before preparing financial statements, adjustments must be made to ensure revenues and expenses are recorded in the correct period. This topic covers accruals vs cash accounting, bad debts, depreciation, capital vs revenue expenditure, and inventory valuation.

---

## 1. Cash vs Accrual Accounting

| Method | Records when... | Used for |
|--------|-----------------|----------|
| **Cash accounting** | Cash is received/paid | Small businesses, tax purposes |
| **Accrual accounting** | Revenue is earned / expense is incurred | Financial reporting (required by standards) |

> [!important] Key Principle
> Financial statements must be prepared on the **accrual basis** — match revenues to the period they relate to, and match expenses to the period they help generate revenue.

### Types of Adjustments

| Adjustment | Description |
|------------|-------------|
| **Accrued expenses** | Expenses incurred but not yet paid |
| **Accrued income** | Revenue earned but not yet received |
| **Prepaid expenses** | Expenses paid in advance |
| **Unearned revenue** | Revenue received in advance |

---

## 2. Bad Debts and Allowance for Doubtful Accounts

| Term | Definition |
|------|------------|
| **Bad debt** | A receivable that is confirmed uncollectible |
| **Allowance for doubtful accounts** | An estimate of future uncollectible receivables |

### Journal Entries

**Writing off a bad debt:**
| Account | Dr | Cr |
|---------|----|----|
| Bad debts (Expense ↑) | X | |
| Trade receivables (Asset ↓) | | X |

**Creating/reducing allowance:**
| Account | Dr | Cr |
|---------|----|----|
| Allowance adjustment (Expense ↑) | X | |
| Allowance for doubtful accounts (Contra-asset ↑) | | X |

> [!example] Worked Example
> Trade receivables = \$50,000. Allowance for doubtful accounts = 5% = \$2,500.
>
> If the allowance was \$2,000 last year, the increase is \$500.
> - Dr Allowance adjustment (Income statement): \$500
> - Cr Allowance for doubtful accounts (SFP): \$500
>
> Net receivables on SFP = \$50,000 − \$2,500 = **\$47,500**

---

## 3. Depreciation

> [!note] Definition
> **Depreciation** is the systematic allocation of the cost of a non-current asset over its useful life. It reflects the wear and tear, obsolescence, or usage of the asset.

### Methods of Depreciation

| Method | Formula | Best For |
|--------|---------|----------|
| **Straight-line** | $\frac{\text{Cost} - \text{Residual value}}{\text{Useful life}}$ | Assets with uniform usage |
| **Reducing balance** | $\text{NBV at start of year} \times \text{Rate\%}$ | Assets that lose value quickly |
| **Units of production** | $\frac{\text{Cost} - \text{Residual value}}{\text{Total estimated units}} \times \text{Units produced}$ | Assets with variable usage |

### Journal Entry

| Account | Dr | Cr |
|---------|----|----|
| Depreciation expense (Expense ↑) | X | |
| Accumulated depreciation (Contra-asset ↑) | | X |

### Disposal of Asset

When an asset is sold:

1. Update depreciation to date of disposal
2. Remove cost and accumulated depreciation
3. Record sale proceeds
4. Calculate and record **gain or loss on disposal**

| Account | Dr | Cr |
|---------|----|----|
| Cash/Bank (received) | X | |
| Accumulated depreciation | X | |
| Loss on disposal (if any) | X | |
| Non-current asset (cost) | | X |
| Gain on disposal (if any) | | X |

> [!tip] Exam Tip
> Depreciation affects BOTH the income statement (as an expense) AND the statement of financial position (reduces net book value of assets). Always show both effects.

---

## 4. Capital vs Revenue Expenditure

| Type | Definition | Treatment |
|------|------------|-----------|
| **Capital expenditure** | Buying/improving non-current assets | Capitalise (record as asset, depreciate) |
| **Revenue expenditure** | Day-to-day operating costs | Expense in income statement |

> [!warning] Misclassification
> If capital expenditure is treated as revenue expenditure, profits are **understated** and assets are **understated**. The reverse is also true.

---

## 5. Inventory Valuation

### Lower of Cost and Net Realisable Value (NRV)

> [!important] IAS 2 / HKAS 2
> Inventory must be valued at the **lower of cost and NRV**. This ensures inventory is not overstated.

- **Cost** = purchase price + import duties + transport + other directly attributable costs
- **NRV** = estimated selling price − estimated costs to complete − estimated costs to sell

### Weighted Average Cost

$$\text{Weighted average cost per unit} = \frac{\text{Total cost of goods available for sale}}{\text{Total units available for sale}}$$

### Sale or Return

Goods dispatched on **sale or return** remain the property of the seller until the buyer confirms acceptance. They should be included in the seller's closing inventory.

---

## Related

- [[Double Entry System]] — The debit/credit rules for adjustments
- [[Financial Reporting by Business Ownership]] — How adjustments feed into financial statements
- [[Financial Analysis and Ratios]] — How adjustments affect ratios
- [[BAFS Index]]
