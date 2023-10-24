def first(get_responce):
    def middleware(request):
        print('before')
        responce = get_responce(request)
        print('after')
        return responce
    
    
    
    return middleware