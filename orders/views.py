from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Order, PointTransaction
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        points_to_use = int(request.data.get('points_used', 0))
        
        if points_to_use > 0 and request.user.points_balance < points_to_use:
            return Response({'error': 'Not enough points!'}, status=status.HTTP_400_BAD_REQUEST)
            
        response = super().create(request, *args, **kwargs)
        
        if points_to_use > 0:
            order = Order.objects.get(id=response.data['id'])
            request.user.points_balance -= points_to_use
            request.user.save()
            
            PointTransaction.objects.create(
                customer=request.user,
                order=order,
                points=-points_to_use,
                transaction_type='Redeemed'
            )
        return response