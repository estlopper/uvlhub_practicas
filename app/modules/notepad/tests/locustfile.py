from locust import HttpUser, TaskSet, task
from core.environment.host import get_host_for_locust_testing


class NotepadBehavior(TaskSet):
    def on_start(self):
        self.index()

    @task(2)
    def index(self):
        response = self.client.get("/notepad")

        if response.status_code != 200:
            print(f"Notepad index failed: {response.status_code}")

    @task(1)
    def create_notepad(self):
        response = self.client.post("/notepad/create", json={"title": "Notepad generado por Locust", "body": "Contenido de prueba"})
        if response.status_code == 201:
            print("Notepad creado correctamente.")
        else:
            print(f"Error al crear el notepad: {response.status_code}")
            
    @task(1)
    def get_notepad(self):
        response = self.client.get("/notepad/1")
        if response.status_code == 200:
            print("Notepad obtenido correctamente.")
        else:
            print(f"Error al obtener el notepad: {response.status_code}")
            
    @task(1)
    def edit_notepad(self):
        response = self.client.post("/notepad/edit/1", json={"title": "Notepad editado por Locust", "body": "Contenido editado de prueba"})
        if response.status_code == 200:
            print("Notepad editado correctamente.")
        else:
            print(f"Error al editar el notepad: {response.status_code}")
        
    @task(1)
    def delete_notepad(self):
        response = self.client.post("/notepad/delete/1")
        if response.status_code == 204:
            print("Notepad eliminado correctamente.")
        else:
            print(f"Error al eliminar el notepad: {response.status_code}")
            
            
class NotepadUser(HttpUser):
    tasks = [NotepadBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()
