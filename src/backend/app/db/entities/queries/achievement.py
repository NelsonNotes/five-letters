from app.db.connection import SessionLocal


class DatabaseBillCRUD:
    def create_bill(bill: schemas.Bill):
        db = SessionLocal()
        bill_dict = bill.__dict__.copy()
        for key in bill.__dict__.keys():
            if key.startswith('_') or key == 'id':
                bill_dict.pop(key)
        db_bill = models.Bill(**bill_dict)
        db.add(db_bill)
        db.commit()
        db.refresh(db_bill)
        db.close()
        return db_bill

    def read_bill_by_id(bill_id: str):
        db = SessionLocal()
        db_bill = db.query(models.Bill).filter(
            models.Bill.billId == bill_id).first()
        db.close()
        return db_bill

    def read_bills(limit: int | None = None):
        db = SessionLocal()
        db_bill = db.query(models.Bill).limit(limit).all()
        db.close()
        return db_bill

    def update_bill(bill: schemas.Bill):
        db = SessionLocal()
        db_bill = db.query(models.Bill).filter(
            models.Bill.billId == bill.billId).first()
        db_bill.siteId = bill.siteId
        db_bill.billId = bill.billId
        db_bill.amount = bill.amount
        db_bill.status = bill.status
        db_bill.creationDateTime = bill.creationDateTime
        db_bill.expirationDateTime = bill.expirationDateTime
        db_bill.payUrl = bill.payUrl
        db_bill.login = bill.login
        db_bill.tax = bill.tax
        db_bill.buy_rate = bill.buy_rate
        db_bill.sell_rate = bill.sell_rate
        db_bill.costs = bill.costs
        db.commit()
        db.refresh(db_bill)
        db.close()
        return db_bill

    def delete_bill(bill: schemas.Bill):
        db = SessionLocal()
        db_bill = db.query(models.Bill).filter(
            models.Bill.billId == bill.billId).first()
        db.delete(db_bill)
        db.commit()
        db.close()
        return True


class DatabaseArchiveCRUD:
    def create_bill(bill: schemas.Bill):
        db = SessionLocal()
        bill_dict = bill.__dict__.copy()
        for key in bill.__dict__.keys():
            if key.startswith('_') or key == 'id':
                bill_dict.pop(key)
        db_bill = models.BillHistory(**bill_dict)
        db.add(db_bill)
        db.commit()
        db.refresh(db_bill)
        db.close()
        return db_bill

    def read_bill_by_id(bill_id: str):
        db = SessionLocal()
        db_bill = db.query(models.BillHistory).filter(
            models.Bill.billId == bill_id).first()
        db.close()
        return db_bill

    def read_bills(limit: int | None = None):
        db = SessionLocal()
        db_bill = db.query(models.BillHistory).limit(limit).all()
        db.close()
        return db_bill

    def update_bill(bill: schemas.Bill):
        db = SessionLocal()
        db_bill = db.query(models.BillHistory).filter(
            models.BillHistory.billId == bill.billId).first()
        db_bill.siteId = bill.siteId
        db_bill.billId = bill.billId
        db_bill.amount = bill.amount
        db_bill.status = bill.status
        db_bill.creationDateTime = bill.creationDateTime
        db_bill.expirationDateTime = bill.expirationDateTime
        db_bill.payUrl = bill.payUrl
        db_bill.login = bill.login
        db_bill.tax = bill.tax
        db_bill.buy_rate = bill.buy_rate
        db_bill.sell_rate = bill.sell_rate
        db_bill.costs = bill.costs
        db.commit()
        db.refresh(db_bill)
        db.close()
        return db_bill

    def delete_bill(bill: schemas.Bill):
        db = SessionLocal()
        db_bill = db.query(models.BillHistory).filter(
            models.BillHistory.billId == bill.billId).first()
        db.delete(db_bill)
        db.commit()
        db.close()
        return True
