"""DDT implements."""
import xlrd


class DDT():
    """Support simple excel reading functions."""

    def __init__(self, file_path, sheet='Sheet1'):
        """Init method to open the excel file."""
        self.data = xlrd.open_workbook(file_path)
        self.table = self.data.sheet_by_name(sheet)
        self.row = self.table.row_values(0)
        self.row_num = self.table.nrows
        self.col_num = self.table.ncols
        self.cur_row_no = 1

    def get_data_from_file(self):
        """Get test data from file."""
        r = []
        while self.has_next(self.row_num, self.cur_row_no):
            s = {}
            col = self.table.row_values(self.cur_row_no)
            i = self.col_num
            for x in range(i):
                s[self.row[x]] = col[x]
                if self.row[x].endswith(u'_date'):
                    s[self.row[x]] = xlrd.xldate_as_tuple(col[x], 0)
            r.append(s)
            self.cur_row_no += 1
        return r

    def has_next(self, row_num, cur_row_no):
        """Return if have next."""
        if row_num == 0 or row_num <= cur_row_no:
            return False
        else:
            return True
