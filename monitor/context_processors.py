from monitor.models import Server, ServerUser


def server(request):
    current_user = request.user
    server_userobj = ServerUser.objects.filter(user_id=current_user.id).exists()  # check server user pairing
    if server_userobj:
        servers = []
        # select * from Server_User where user_id=current_user.id
        server = ServerUser.objects.filter(user_id=current_user.id).values_list('server_id', flat=True)
        for i in range(len(server)):
            servers.append(Server.objects.get(id=server[i]))  # added server ids in servers array.
        return {'servers': servers}
    else:
        return {'servers': "is null"}
