from passlib.context import CryptContext



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #We are just asking passlib what hashing mechnism we are using which is bcrypt

def hash(password: str):
    return pwd_context.hash(password)
