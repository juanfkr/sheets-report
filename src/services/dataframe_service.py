from pandas import DataFrame

class DataFrameService:
    def __init__(self, data_frame: DataFrame):
        self.data_frame = data_frame

    # TODO: novo dataframe com dados tratados a partir do DF populacionado
    # deve incluir:
    # OrderID | OrderDate | CustomerName | ProductID | ProductName | Category | Brand | Quantity
    # UnitPrice | Discount | Tax | ShippingCost | TotalAmount | PaymentMethod | OrderStatus |
    # City | State | Country
    def sanitized_dataframe(self):
        pass