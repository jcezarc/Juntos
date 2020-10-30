from service.db.loader import Loader, FilterException


class CustomerService:

    def find(self, args):
        try:
            found = self.pagination(args)
        except FilterException:
            return 'Falta informar regiao ou tipo de usuario.', 400
        if not found:
            return 'Nenhum registro encontrado.', 404
        return found, 200

    def pagination(self, args):
        result = {}
        Loader.filter(
            region=args.get('region'),
            user_type=args.get('type'),
        )
        total_count = Loader.record_count()
        if total_count < 1:
            return None
        page_number = int(args.get('pageNumber', 1))
        page_size = int(args.get('pageSize', 10))
        result['pageNumber'] = page_number
        result['pageSize'] = page_size
        result['totalCount'] = total_count
        users = []
        i = (page_number-1) * page_size
        while len(users) < page_size:
            record = Loader.fetch_one(i)
            if not record:
                break
            users.append(record)
            i += 1
        result['users'] = users
        return result
