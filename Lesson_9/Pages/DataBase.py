from sqlalchemy import create_engine,text

class DataBase:
    query = {
        'create_company': text('INSERT INTO company(name, description) VALUES (:name, :description)'),
        'max_company': text('SELECT MAX(id) FROM company'),
        'delete_company': text('DELETE FROM company WHERE id = :company_id'),
        'list_SELECT': text('SELECT * FROM employee WHERE company_id = :id'),
        'item_SELECT': text('SELECT * FROM employee WHERE company_id = :c_id AND id = :e_id'),
        'maxID_SELECT': text('SELECT MAX(id) FROM employee WHERE company_id = :c_id'),
        'item_DELETE': text('DELETE FROM employee WHERE id = :id_delete'),
        'item_UPDATE': text('UPDATE employee SET first_name = :new_name WHERE id = :employer_id'),
        'item_INSERT': text('INSERT INTO employee(company_id, first_name, last_name, phone) VALUES(:id, :name, :surname, :phone)')
    }

    def __init__(self, engine) -> None:
        self.db = create_engine(engine)

    # создаем компанию в базе данных
    def create_company(self, company_name: str, description):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['create_company'], parameters=dict(name=company_name, description=description ))
                connection.commit()
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if 'connection' in locals():
                connection.close()
                print("[INFO] DB connection closed")

    # получаем id последней созданной компании
    def last_company_id(self):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['max_company']).fetchall()[0][0]
                return result
        except Exception as _ex:
            print("[INFO] Ошибка - невозможно работать с SQL", _ex)
        finally:
            print("[INFO] Соединение с БД закрыто")

    # получаем сотрудников из базы данных
    def get_list_employer(self, company_id: int):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['list_SELECT'], parameters=dict(id = company_id) ).fetchall()
                return result
        except Exception as _ex:
            print("[INFO] Ошибка - невозможно работать с SQL", _ex)
        finally:
            print("[INFO] Соединение с БД закрыто")

    # создаем сотрудника       
    def create_employer(self, company_id: int, first_name: str, last_name: str, phone: str):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['item_INSERT'], parameters=dict(id = company_id, name = first_name, surname = last_name,phone_num = phone) )
                connection.commit()
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if 'connection' in locals():
                connection.close()
                print("[INFO] DB connection closed")

    # получаем id сотрудника
    def get_employer_id(self, company_id: int):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['maxID_SELECT'],parameters=dict(c_id = company_id) ).fetchall()[0][0]
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if 'connection' in locals():
                connection.close()
                print("[INFO] DB connection closed")

    # изменяем информацию о сотруднике
    def update_employer_info(self, new_name: str, id: int):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['item_UPDATE'], parameters=dict(new_name = new_name, employer_id = id) )
                connection.commit()
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if 'connection' in locals():
                connection.close()
                print("[INFO] DB connection closed")

    # удаляем сотрудника
    def delete_employer(self, id: int):
        try:
            with self.db.connect() as connection:
                result = connection.execute(self.query['item_DELETE'],parameters=dict(id_delete = id)  )
                connection.commit()
                return result
        except Exception as _ex:
            print("[INFO] Error - can't work with SQL", _ex)
        finally:
            if 'connection' in locals():
                connection.close()
                print("[INFO] DB connection closed")

