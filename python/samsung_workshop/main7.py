def logit(start_msg="started", stop_msg="stopped"):
  def logit_decorate(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
          print("started ()".format(start_msg,func.__name__))
          return_value=func(*args,**kwargs)
          print("finished ()".format(stop_msg,func.__name__))
          return return_value
      return wrapper
    return logit_decorate

def bar():
    print("bar")

wrapped=
