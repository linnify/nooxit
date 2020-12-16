from fastapi import APIRouter
from app.db import users
from app.db import members

router = APIRouter()


@router.get('/users')
def get_users():
    """
    Return the users only if the user has been granted with user scope
     :return: all the users
    """
    
    return users.get_all_users()


@router.get('/members')
def get_members():
    """
    Return the profiles only if the user has been granted with user scope
    :return: all the members
    """
    
    return members.get_all_members()
