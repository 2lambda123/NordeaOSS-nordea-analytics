from enum import Enum


class BondKeyFigureName(Enum):
    """Control which bond key figure names are available in the service."""

    AccruedInterest = "accint"
    AssetSwapSpread = "asw"
    BPV10Y = "bpv10y"
    BPV15Y = "bpv15y"
    BPV1Y = "bpv1y"
    BPV20Y = "bpv20y"
    BPV25Y = "bpv25y"
    BPV2Y = "bpv2y"
    BPV30Y = "bpv30y"
    BPV3M = "bpv3m"
    BPV5Y = "bpv5y"
    BPV6M = "bpv6m"
    BPV7Y = "bpv7y"
    BPVP = "bpvp"
    CleanPrice = "clean_price"
    ClosingDate = "closing_date"
    Coupon = "coupon"
    Currency = "currency"
    CVXP = "cvxp"
    ExPrincipalDate = "exprincipaldate"
    FWDuration_Deterministic = "fwduration"
    HistoricalReturnAccumulated = "dd_total_acc"
    HorizonReturn12M = "return12m"
    HorizonReturn12M100 = "return12m100"
    HorizonReturn12M25 = "return12m25"
    HorizonReturn12M50 = "return12m50"
    HorizonReturn12M75 = "return12m75"
    HorizonReturn12Mm100 = "return12m-100"
    HorizonReturn12Mm25 = "return12m-25"
    HorizonReturn12Mm50 = "return12m-50"
    HorizonReturn12Mm75 = "return12m-75"
    HorizonReturn3M = "return3m"
    HorizonReturn3M50 = "return3m50"
    HorizonReturn3Mm50 = "return3m-50"
    HorizonReturn6M = "return6m"
    HorizonReturn6M50 = "return6m50"
    HorizonReturn6Mm50 = "return6m-50"
    HorizonReturnCapital12M = "capital12m"
    HorizonReturnCapital12M100 = "capital12m100"
    HorizonReturnCapital12M25 = "capital12m25"
    HorizonReturnCapital12M50 = "capital12m50"
    HorizonReturnCapital12M75 = "capital12m75"
    HorizonReturnCapital12Mm100 = "capital12m-100"
    HorizonReturnCapital12Mm25 = "capital12m-25"
    HorizonReturnCapital12Mm50 = "capital12m-50"
    HorizonReturnCapital12Mm75 = "capital12m-75"
    HorizonReturnCapital3M = "capital3m"
    HorizonReturnCapital3M50 = "capital3m50"
    HorizonReturnCapital3Mm50 = "capital3m-50"
    HorizonReturnCapital6M = "capital6m"
    HorizonReturnCapital6M50 = "capital6m50"
    HorizonReturnCapital6Mm50 = "capital6m-50"
    HorizonReturnInterest12M = "interest12m"
    HorizonReturnInterest12M100 = "interest12m100"
    HorizonReturnInterest12M25 = "interest12m25"
    HorizonReturnInterest12M50 = "interest12m50"
    HorizonReturnInterest12M75 = "interest12m75"
    HorizonReturnInterest12Mm100 = "interest12m-100"
    HorizonReturnInterest12Mm25 = "interest12m-25"
    HorizonReturnInterest12Mm50 = "interest12m-50"
    HorizonReturnInterest12Mm75 = "interest12m-75"
    HorizonReturnInterest3M = "interest3m"
    HorizonReturnInterest3M50 = "interest3m50"
    HorizonReturnInterest3Mm50 = "interest3m-50"
    HorizonReturnInterest6M = "interest6m"
    HorizonReturnInterest6M50 = "interest6m50"
    HorizonReturnInterest6Mm50 = "interest6m-50"
    HorizonReturnTNS12M = "returntns12m"
    HorizonReturnTNS1M = "returntns1m"
    HorizonReturnTNS3M = "returntns3m"
    MacauleyDuration_Deterministic = "macauley_duration"
    Maturity = "maturity"
    MaxOutstandingAmount = "max_outstanding_amount"
    ModifiedDuration_Deterministic = "modduration"
    NoTerms = "no_terms"
    NotificationDate = "notificationdate"
    OAS_GOV = "govoas"
    OAModifiedDuration = "modified_bpv"
    OASRisk = "oasrisk"
    OAS_OIS = "oas"
    OAS_3M = "libor_3m_spread"
    OAS_6M = "libor_spread"
    OATheta = "oatheta"
    OfficialPrice = "official_price"
    OpeningDate = "opening_date"
    OutstandingAmount = "outstanding_amount"
    OutstandingAmountCorrected = "corrected_outstanding_amount"
    PaymentScheduled = "schedpayment"
    PaymentTotal = "totpaymentamt"
    PrePayment = "prepublished_prepayment"
    PrePaymentPercentage = "prepayment"
    PrePaymentPreliminary = "prelimprepayment"
    PrePaymentPreliminaryPercentage = "ppp"
    PresentValue = "present_value"
    Pricem100 = "pm100"
    Pricem200 = "pm200"
    Pricem300 = "pm300"
    Pricem400 = "pm400"
    Pricem50 = "pm50"
    Pricep100 = "pp100"
    Pricep200 = "pp200"
    Pricep300 = "pp300"
    Pricep400 = "pp400"
    Pricep50 = "pp50"
    Quote = "quote"
    QuotedSize = "quotedsize"
    SettlementDays = "settlement_days"
    Spread = "spread"
    SpreadRisk = "spreadrisk"
    SwapSpread = "swap_spread"
    TermsPrYear = "terms_per_year"
    Theta = "theta"
    Vega = "vega"
    WAL_Deterministic = "detwal"
    YCSGOV_Deterministic = "govycs"
    YCS_OIS_Deterministic = "ycs"
    Yield_Deterministic = "yield"


class TimeSeriesKeyFigureName(Enum):
    """Control which time series key figure names are available in the service."""

    AccruedInterest = "accint"
    AssetSwapSpread = "asw"
    BPV10Y = "bpv10y"
    BPV15Y = "bpv15y"
    BPV1Y = "bpv1y"
    BPV20Y = "bpv20y"
    BPV25Y = "bpv25y"
    BPV2Y = "bpv2y"
    BPV30Y = "bpv30y"
    BPV3M = "bpv3m"
    BPV5Y = "bpv5y"
    BPV6M = "bpv6m"
    BPV7Y = "bpv7y"
    BPVP = "bpvp"
    CVXP = "cvxp"
    Duration = "duration"
    FWDuration_Deterministic = "fwduration"
    GovSpread = "gov_spread"
    HistoricalCapitalGain = "dd_princ"
    HistoricalReturn = "dd_total"
    HistoricalReturnAccumulated = "dd_total_acc"
    HorizonReturn12M = "return12m"
    HorizonReturn12M100 = "return12m100"
    HorizonReturn12M25 = "return12m25"
    HorizonReturn12M50 = "return12m50"
    HorizonReturn12M75 = "return12m75"
    HorizonReturn12Mm100 = "return12m-100"
    HorizonReturn12Mm25 = "return12m-25"
    HorizonReturn12Mm50 = "return12m-50"
    HorizonReturn12Mm75 = "return12m-75"
    HorizonReturn3M = "return3m"
    HorizonReturn3M50 = "return3m50"
    HorizonReturn3Mm50 = "return3m-50"
    HorizonReturn6M = "return6m"
    HorizonReturn6M50 = "return6m50"
    MacauleyDuration_Deterministic = "macauley_duration"
    ModifiedDuration = "modified_bpv"
    ModifiedDuration_Deterministic = "modduration"
    OutstandingAmount = "outstanding_amount"
    OutstandingAmountCorrected = "corrected_outstanding_amount"
    PriceAvg = "average_price_all_deals"
    PriceClean = "price"
    PriceClosing = "kf_closing_price"
    PriceDirty = "present_value"
    PriceKF = "official_price"
    PriceSpread = "price_spread"
    PriceTheo = "theoretical_price"
    Quote = "quote"
    Spread = "spread"
    SpreadLibor = "libor_spread"
    SpreadLibor3M = "libor_3m_spread"
    SpreadRisk = "spreadrisk"
    SwapSpread = "swap_spread"
    Theta = "theta"
    TurnoverDaily = "turnover_all_deals"
    Vega = "vega"
    Wal = "wal"
    WAL_Deterministic = "detwal"
    YCS_OIS_Deterministic = "ycs"
    YCSGOV_Deterministic = "govycs"
    Yield_Deterministic = "yield"


class CalculatedBondKeyFigureName(Enum):
    """Control which bond key figure names can be calculated in the service."""

    ASW_MM = "aswmm"
    ASW = "asw"
    ASW_PP = "aswpp"
    BPV_Ladder = "bpvladder"
    BPV = "bpv"
    CVX = "cvx"
    MacaulayDuration = "macdur"
    ModifiedDuration = "moddur"
    Spread = "spread"
    SpreadRisk = "spreadrisk"
    Price = "price"
    Yield = "yield"


class HorizonCalculatedBondKeyFigureName(Enum):
    """Control which bond key figure names can be horizon calculated in the service."""

    BPV = "bpv"
    CVX = "cvx"
    Price = "price"
    Spread = "spread"


class LiveBondKeyFigureName(Enum):
    """Control which bond key figure names are available live in the service."""

    CVX = "cvx"
    Spread = "spread"
    Yield = "yield"
    Quote = "quote"
    BPV = "bpv"
    SwapSpread = "swap spread"
    OAS_3M = "libor 3m spread"
    OAS_6M = "libor 6m spread"
    GovSpread = "gov spread"