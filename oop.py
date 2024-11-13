class HocVien():
    def __init__(self,maHV,tenHV,ngaySinh,khoaHoc=[]):
        self.maHV = maHV
        self.tenHV =tenHV
        self.ngaySinh =ngaySinh
        self.khoaHoc = [khoaHoc]  
    def dangKyKhoaHoc(self, khoaHocMoi):
        return self.khoaHoc.append(khoaHocMoi)
    def hienHocVien(self):
        print(f"hoc vien {self.maHV}\n tenHV: {self.tenHV}\nngaysinhoc: {self.ngaySinh}\nkhoaHoc: {self.khoaHoc}")
        
class KhoaHoc():
    def __init__(self,maKhoaHoc,tenKhoaHoc,hinhThuc,hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc =hinhThuc
        self.hocPhi = hocPhi
    def thongTinKhoaHoc(self):
        return f"Ma khoa hoc: {self.maKhoaHoc}\nTen khoa hoc: {self.tenKhoaHoc}\nHinh thuc: {self.hinhThuc}\n Hoc phi: {self.hocPhi}\n"
        
kh1=KhoaHoc(13,"lt","on",23000)
kh2=KhoaHoc(23,"bj","off",35555)
hv1=HocVien(12,"nguyen van a","24/4/2444","lap trinh")
hv2=HocVien(11,"nguyen van b","24/4/2344","lap tr c")
hv1.dangKyKhoaHoc("cs2")
print(f"hien thi thon tin hv:{hv1.hienHocVien()}")



        