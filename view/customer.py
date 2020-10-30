from flask import request, current_app
from flask_restful import Resource
from service.customer import CustomerService

class CustomerResource(Resource):
    def get(self):
        available = current_app.config.get('available', False)
        if not available:
            return 503, 'O serviço ainda não está disponível.'
        service = CustomerService()
        return service.find(request.args)
