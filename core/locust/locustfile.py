from locust import HttpUser, task, between

class BlogUser(HttpUser):
    
    # wait_time = between(1, 3)
    def on_start(self):
       response = self.client.post('/accounts/api/v1/jwt/create/' , data=
        {
            'username': 'amir',
            'password': 'amirmad2007',
        }).json()
       self.client.headers = {'Authorization': f'Bearer {response.get('access' , None)}'}

    @task
    def post_list(self):
        self.client.get("/blog/api/v1/post/")

    @task
    def category_lit(self):
        self.client.get("/blog/api/v1/category/")
    
    # @task(1)
    # def get_post_detail(self):
    #     self.client.get("/blog/api/v1/post/1/")
