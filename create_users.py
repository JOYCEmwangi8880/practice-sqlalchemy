from sqlalchemyex import User,Session,engine


users=[
    {
        'username':'joy',
        'email':'joy@company.com'
    },
     {
        'username':'evans',
        'email':'evani@company.com'
    },
     {
        'username':'matt',
        'email':'matt@company.com'
    },
     {
        'username':'maggy',
        'email':'maggy@company.com'
    },
     {
        'username':'ann',
        'email':'ann@company.com'
    },
     {
        'username':'ayub',
        'email':'ayub@company.com'
    }
]







local_session=Session(bind=engine)


# new_user=User(username='wangui',email='wangui2023@gmail.com')

# local_session.add(new_user)

# local_session.commit()

for user in users:
    new_user=User(username=user['username'],email=user['email'])
    print(new_user)

    local_session.add(new_user)

    local_session.commit()
    
    print (f"Added {user['username']}")