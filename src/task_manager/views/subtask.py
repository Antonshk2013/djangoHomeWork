from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.task_manager.services import SubTaskService
from src.common.services import ErrorType


class BaseSubTask(APIView):
    service = SubTaskService()


class SubTaskListCreateView(BaseSubTask):

    def post(self, request):
        result = self.service.create(request.data)
        if result.success:
            return Response(
                data=result.data,
                status=status.HTTP_200_OK
            )
        elif result.error_type == ErrorType.VALIDATION_ERROR:
            return Response(
                data=result.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            data=result.errors,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )



    def get(self, request):
        result = self.service.get_all_subtasks()
        if result.success:
            return Response(
                data=result.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data=result.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class SubTaskDetailUpdateDeleteView(BaseSubTask):

    def get(self, request: Request, subtask_id: int) -> Response:
        ...

    def put(self, request: Request, subtask_id: int) -> Response:
        ...

    def delete(self, request: Request, subtask_id: int) -> Response:
        ...