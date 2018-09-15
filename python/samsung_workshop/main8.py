from functools import wraps

def retry_on_exception(exception, retry_count=2):
  def logit_decorate(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        while retry_count>0:
          try:
              return_value=func(*args,**kwargs)
              return return_value

          except exception:
              retry_count -= 1

              if retry_count >= 0:
                  return_value=func(*args, **kwargs)
              else:
                  print(exception)
          return return_value
      return wrapper
    return logit_decorate



@retry_on_exception(exception=(TimeoutException, IndexError), retry_count=2)
def connect(self):
    self.open_connection(self.host)
