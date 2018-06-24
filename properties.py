# -*- coding: utf-8 -*-


class LogisticsType:
    CVS = "CVS"
    HOME = "HOME"


class LogisticsSubType:
    ### CVS ###
    FAMI = "FAMI"               # 全家物流(B2C)
    UNIMART = "UNIMART"         # 統一超商物流(B2C)
    FAMIC2C = "FAMIC2C"         # 全家物流(C2C)
    UNIMARTC2C = "UNIMARTC2C"   # 統一超商物流(C2C)
    HILIFE = "HILIFE"           # 萊爾富物流(B2C)
    HILIFEC2C = "HILIFEC2C"     # 萊爾富物流(C2C)

    ### HOME ###
    TCAT = "TCAT"               #黑貓物流
    ECAN = "ECAN"               # 宅配通


class IsCollection:
    Y = "Y"
    N = "N"
