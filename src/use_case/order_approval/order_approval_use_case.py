from src.repository.order_repository import OrderRepository
from .order_approval_request import OrderApprovalRequest


class OrderApprovalUseCase:
    def __init__(self, order_repository: OrderRepository) -> None:
        self._order_repository = order_repository

    def run(self, request: OrderApprovalRequest) -> None:
        order = self._order_repository.get_by_id(request.order_id)

        order.approve() if request.approved else order.reject()

        self._order_repository.save(order)
