xbrl_content_list = [
    # 売上
    {
        "tag": "jppfs_cor:NetSales",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "plResult",
        "item": "netSales",
    },
    # 営業収益
    {
        "tag": "jppfs_cor:OperatingRevenue1",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "plResult",
        "item": "operatingRevenue1",
    },
    # 粗利益
    {
        "tag": "jppfs_cor:GrossProfit",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "plResult",
        "item": "grossProfit",
    },
    # 営業利益
    {
        "tag": "jppfs_cor:OperatingIncome",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "plResult",
        "item": "operatingIncome",
    },
    # 経常利益
    {
        "tag": "jppfs_cor:OrdinaryIncome",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "plResult",
        "item": "ordinaryIncome",
    },
    # 税引き前利益
    {
        "tag": "jppfs_cor:IncomeBeforeIncomeTaxes",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "plResult",
        "item": "incomeBeforeIncomeTaxes",
    },
    # 当期純利益
    {
        "tag": "jppfs_cor:ProfitLoss",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "plResult",
        "item": "profitLoss",
    },
    # 減価償却費
    {
        "tag": "jppfs_cor:DepreciationAndAmortizationOpeCF",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "cashFlowResult",
        "item": "depreciationAndAmortization",
    },
    # 減損損失
    {
        "tag": "jppfs_cor:ImpairmentLossOpeCF",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "cashFlowResult",
        "item": "impairmentLoss",
    },
    # 営業活動によるキャッシュフロー
    {
        "tag": "jppfs_cor:NetCashProvidedByUsedInOperatingActivities",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "cashFlowResult",
        "item": "operatingActivities",
    },
    # 投資活動によるキャッシュフロー
    {
        "tag": "jppfs_cor:NetCashProvidedByUsedInInvestmentActivities",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "cashFlowResult",
        "item": "investmentActivities",
    },
    # 財務活動によるキャッシュフロー
    {
        "tag": "jppfs_cor:NetCashProvidedByUsedInFinancingActivities",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "cashFlowResult",
        "item": "financingActivities",
    },
    # 配当金支払い
    {
        "tag": "jppfs_cor:CashDividendsPaidFinCF",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "cashFlowResult",
        "item": "dividendsPaid",
    },
    # 設備投資
    {
        "tag": "jpcrp_cor:CapitalExpendituresOverviewOfCapitalExpendituresEtc",
        "context_ref": "CurrentYearDuration",
        "context_ref_nonconsolidatedMember": "CurrentYearDuration_NonConsolidatedMember",
        "statement_type": "cashFlowResult",
        "item": "capitalExpenditures",
    },
    # 流動資産
    {
        "tag": "jppfs_cor:CurrentAssets",
        "context_ref": "CurrentYearInstant",
        "context_ref_nonconsolidatedMember": "CurrentYearInstant_NonConsolidatedMember",
        "statement_type": "bsResult",
        "item": "currentAssets",
    },
    # 現金同等物
    {
        "tag": "jppfs_cor:CashAndCashEquivalents",
        "context_ref": "CurrentYearInstant",
        "context_ref_nonconsolidatedMember": "CurrentYearInstant_NonConsolidatedMember",
        "statement_type": "bsResult",
        "item": "cash",
    },
    # 売掛金
    {
        "tag": "jppfs_cor:AccountsReceivableTrade",
        "context_ref": "CurrentYearInstant",
        "context_ref_nonconsolidatedMember": "CurrentYearInstant_NonConsolidatedMember",
        "statement_type": "bsResult",
        "item": "accountsReceivable",
    },
    # 投資有価証券
    {
        "tag": "jppfs_cor:InvestmentSecurities",
        "context_ref": "CurrentYearInstant",
        "context_ref_nonconsolidatedMember": "CurrentYearInstant_NonConsolidatedMember",
        "statement_type": "bsResult",
        "item": "investmentSecurities",
    },
    # 資産
    {
        "tag": "jppfs_cor:Assets",
        "context_ref": "CurrentYearInstant",
        "context_ref_nonconsolidatedMember": "CurrentYearInstant_NonConsolidatedMember",
        "statement_type": "bsResult",
        "item": "assets",
    },
    # 株主資本
    {
        "tag": "jppfs_cor:NetAssets",
        "context_ref": "CurrentYearInstant",
        "context_ref_nonconsolidatedMember": "CurrentYearInstant_NonConsolidatedMember",
        "statement_type": "bsResult",
        "item": "netAssets",
    },
    # 負債
    {
        "tag": "jppfs_cor:Liabilities",
        "context_ref": "CurrentYearInstant",
        "context_ref_nonconsolidatedMember": "CurrentYearInstant_NonConsolidatedMember",
        "statement_type": "bsResult",
        "item": "liabilities",
    },
    # -------------------------------------------
    # 短期借入金
    {
        "tag": "jppfs_cor:ShortTermBorrowings",
        "context_ref": "CurrentYearInstant",
        "context_ref_nonconsolidatedMember": "CurrentYearInstant_NonConsolidatedMember",
        "statement_type": "bsResult",
        "item": "shortTermBorrowings",
    },
    # 1年以内返済予定の長期借入金
    {
        "tag": "jppfs_cor:LongTermBorrowingsPayableWithinOneYear",
        "context_ref": "CurrentYearInstant",
        "context_ref_nonconsolidatedMember": "CurrentYearInstant_NonConsolidatedMember",
        "statement_type": "bsResult",
        "item": "longTermBorrowingsPayableWithinOneYear",
    },
    # 長期借入金
    {
        "tag": "jppfs_cor:LongTermBorrowings",
        "context_ref": "CurrentYearInstant",
        "context_ref_nonconsolidatedMember": "CurrentYearInstant_NonConsolidatedMember",
        "statement_type": "bsResult",
        "item": "longTermBorrowings",
    },
]
