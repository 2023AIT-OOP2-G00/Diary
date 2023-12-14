from diaries.AbstractDiary import AbstractDiary

class NagataniDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    
    def get_summary(self):
        return "人数多くてびっくりした。普段から出席して欲しい。"
    
    def get_author(self):
        return "Nagatani"