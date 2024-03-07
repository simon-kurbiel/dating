from fastapi import status, HTTPException

class HTTPEceptionsAPI:
    
    
    def Base(self, msg : str, success:bool = False, status_code: status = status.HTTP_400_BAD_REQUEST):
        detail = {
            'success' : success,
            'message' :f'{msg}'
                  
        }
        raise HTTPException(status_code=status_code, detail=detail)
    
    def HTTPConflictException(self,msg:str):
   
    
        return self.Base(msg=msg, status_code=status.HTTP_409_CONFLICT)
    
    def HTTPBadRequestException(self, msg:str):
        return self.Base(msg=msg, status_code=status.HTTP_400_BAD_REQUEST)
    
    def HTTPUnauthenticatedException(self,msg:str):
        return self.Base(msg=msg, status_code=status.HTTP_403_FORBIDDEN)
        
    
exception = HTTPEceptionsAPI()
    
