class Course:
    """課程資料的資料類別。

    Attributes:
        id(``str``): 科號。
        chinese_title(``str``): 課程中文名稱。
        english_title(``str``): 課程英文名稱。
        credit(``str``): 學分數。
        size_limit(``str``): 人限：若為空字串表示無人數限制。
        freshman_reservation(``str``): 新生保留人數：若為0表示無新生保留人數。
        object(``str``): 通識對象：[代碼說明(課務組)](https://curricul.site.nthu.edu.tw/p/404-1208-11133.php)。
        ge_type(``str``): 通識類別。
        language(``str``): 授課語言："中"、"英"。
        note(``str``): 備註。
        suspend(``str``): 停開註記："停開"或空字串。
        class_room_and_time(``str``):教室與上課時間：一間教室對應一個上課時間，中間以tab分隔；多個上課教室以new line字元分開。
        teacher(``str``): 授課教師：多位教師授課以new line字元分開；教師中英文姓名以tab分開。
        prerequisite(``str``): 擋修說明：會有html entities。
        limit_note(``str``): 課程限制說明。
        expertise(``str``): 第一二專長對應：對應多個專長用tab字元分隔。
        program(``str``): 學分學程對應：用半形/分隔。
        no_extra_selection(``str``): 不可加簽說明。
        required_optional_note(``str``): 必選修說明：多個必選修班級用tab字元分隔。
    """

    def __init__(self, init_data: dict) -> None:
        init_data_keys = list(init_data.keys())

        self.id = init_data[init_data_keys[0]]
        self.chinese_title = init_data[init_data_keys[1]]
        self.english_title = init_data[init_data_keys[2]]
        self.credit = init_data[init_data_keys[3]]
        self.size_limit = init_data[init_data_keys[4]]
        self.freshman_reservation = init_data[init_data_keys[5]]
        self.object = init_data[init_data_keys[6]]
        self.ge_type = init_data[init_data_keys[7]]
        self.language = init_data[init_data_keys[8]]
        self.note = init_data[init_data_keys[9]]
        self.suspend = init_data[init_data_keys[10]]
        self.class_room_and_time = init_data[init_data_keys[11]]
        self.teacher = init_data[init_data_keys[12]]
        self.prerequisite = init_data[init_data_keys[13]]
        self.limit_note = init_data[init_data_keys[14]]
        self.expertise = init_data[init_data_keys[15]]
        self.program = init_data[init_data_keys[16]]
        self.no_extra_selection = init_data[init_data_keys[17]]
        self.required_optional_note = init_data[init_data_keys[18]]

    def __repr__(self) -> str:
        return str(vars(self))
