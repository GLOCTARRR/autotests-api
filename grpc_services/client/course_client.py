import grpc

from grpc_services import course_service_pb2
from grpc_services import course_service_pb2_grpc


channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="123456"))
print(f'course_id: "{response.course_id}"\n')
print(f'title: "{response.title}"\n')
print(f'description: "{response.description}"\n')