class Course:

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
        return

    def __repr__(self) -> str:
        return str(vars(self))
