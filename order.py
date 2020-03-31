class Order:
    order_count = 0
    def __init__(self, supplies, dest_coord, dest_name, source_coord, source_name):
        Order.order_count = Order.order_count + 1
        self.id = Order.order_count
        self.supplies = supplies
        self.Source = {
            'name': source_name,
            'coord': source_coord
        }
        self.Dest = {
            'name': dest_name,
            'coord': dest_coord
        }
        
