import fastapi.templating
import sqlite3
import pydantic
import fastapi.responses
def get_connection():
    return sqlite3.connect(
        "students.db"
    )
get_connection()

def create_table():
    connection=get_connection()
    cursor=connection.cursor()
    q="""
    create table if not exists students(
        id integer primary key autoincrement,
        name text not null,
        age integer,
        gender text,
        marks integer,
        course text,
        image text,
        status integer
        )
    """
    cursor.execute(q)
    connection.commit()
    connection.close()
create_table()


templates=fastapi.templating.Jinja2Templates(
    directory='templates'
)

class Student(pydantic.BaseModel):
    name:str
    age:int
    gender:str
    marks:int
    course:str
    image:str
    status:int

app=fastapi.FastAPI()

@app.get('/students')
def home(req:fastapi.Request):
    connection=get_connection()
    cursor=connection.cursor()
    query="select * from students"
    cursor.execute(query)
    students=cursor.fetchall()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name='students.html',
        context={
            'stds':students
        }
    )
    
@app.get('/students/add')
def create_std(req:fastapi.Request):
    return templates.TemplateResponse(
        request=req,
        name='add-student.html',
        context={}
    )
@app.get("/students/{std_id}")
def one_student(req:fastapi.Request,std_id:int):
    connection=get_connection()
    cursor=connection.cursor()
    query="select * from students where id=?"
    cursor.execute(query,(std_id,))
    std=cursor.fetchone()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name='one-std.html',
        context={
            'std':std
        }
    )



@app.post('/students/add')
def add_student(
    name=fastapi.Form(...),
    age=fastapi.Form(...),
    gender=fastapi.Form(...),
    marks=fastapi.Form(...),
    course=fastapi.Form(...),
    image=fastapi.Form(...),
    status=fastapi.Form(...)
):
    values=Student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )
    std={
        'name':name,
        'age':age,
        'gender':gender,
        'marks':marks,
        'course':course,
        'image':image,
        'status':status
    }
    std_details=[values.name,values.age,values.gender,values.marks,values.course,values.image,bool(values.status)]
    q="""
    insert into students (name,age,gender,marks,course,image,status) values
    (?,?,?,?,?,?,?)
    """
    connection=get_connection()
    connection.cursor().execute(q,std_details)
    connection.commit()
    connection.close()
    return fastapi.responses.RedirectResponse(url='/students',status_code=303)

@app.get('/students/{std_id}/update')
def update_std(req:fastapi.Request,std_id:int):
    query="select * from students where id=?"
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute(query,(std_id,))
    std=cursor.fetchone()
    connection.close()
    print(std)
    return templates.TemplateResponse(
        request=req,
        name="update-student.html",
        context={
            "std":std
        }
    )
    
@app.post('/students/{std_id}/update')
def update_student(std_id:int,
                   name=fastapi.Form(...),
                   age=fastapi.Form(),
                   gender=fastapi.Form(),
                   marks=fastapi.Form(),
                   course=fastapi.Form(),
                   image=fastapi.Form(),
                   status=fastapi.Form()):
    values=Student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )
    print(values.name)
    updt_std_details=[values.name,values.age,values.gender,values.marks,values.course,values.image,bool(values.status),std_id]
    query="""
            update students set
            name=?,age=?,gender=?,marks=?,course=?,image=?,status=?
            where id=?
            """
    connection=get_connection()
    connection.cursor().execute(query,updt_std_details)
    connection.commit()
    connection.close()
    return fastapi.responses.RedirectResponse(url="/students",status_code=fastapi.status.HTTP_303_SEE_OTHER)

@app.post("/students/{std_id}/delete")
def delete_student(std_id:int):
    connection=get_connection()
    connection.cursor().execute('delete from students where id=?',(std_id,))
    connection.commit()
    connection.close()
    return fastapi.responses.RedirectResponse(url="/students",
        status_code=303)