from monitor.models import Server, Server_User


def server(request):
    current_user = request.user
    # check server user pairing
    server_userobj = Server_User.objects.filter(
                    user_id=current_user.id).exists()
    if server_userobj:
        servers = []
        # select * from Server_User where user_id=current_user.id
        server = Server_User.objects.filter(
                 user_id=current_user.id).values_list('server_id', flat=True)
        for i in range(len(server)):
            # added server ids in servers array.
            servers.append(Server.objects.get(id=server[i]))
        return {'servers': servers}
    else:
        return {'servers': "is null"}
