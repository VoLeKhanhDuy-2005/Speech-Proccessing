f = open("trial.wav", "rb")
ID = f.read(4)
print("%c%c%c%c" % (ID[0], ID[1], ID[2], ID[3]))

fileSize = f.read(4)# đọc 4 byte
fileSize = fileSize[3]*255**3 + fileSize[2]*256**2 + fileSize[1]*256 + fileSize[0] # đổi hex về dec đã - 8 (kq:1240548 -> properties: 1240556)
print(fileSize)

fileFormatId = f.read(4)
print("%c%c%c%c" % (fileFormatId[0], fileFormatId[1], fileFormatId[2], fileFormatId[3]))

formatBlockId = f.read(4)
print("%c%c%c%c" % (formatBlockId[0], formatBlockId[1], formatBlockId[2], formatBlockId[3]))

blocSize = f.read(4)
blocSize = blocSize[3]*255**3 + blocSize[2]*256**2 + blocSize[1]*256 + blocSize[0]
print("%d" % blocSize)

AudioFormat = f.read(2)
AudioFormat = AudioFormat[1]*256 + AudioFormat[0]
print("Format theo chuẩn PCM là %d" % AudioFormat)# 1 is PCM, 3 is IEEE

NbrChannels = f.read(2)
NbrChannels = NbrChannels[1]*256 + NbrChannels[0]
print("Số lượng kênh là %d" % NbrChannels)

Frequency = f.read(4)
Frequency = Frequency[3]*255**3 + Frequency[2]*256**2 + Frequency[1]*256 + Frequency[0]
print("Tần số lấy mẫu là %d Hz" % Frequency)

BytePerSec = f.read(4)
BytePerSec = BytePerSec[3]*255**3 + BytePerSec[2]*256**2 + BytePerSec[1]*256 + BytePerSec[0]
print("Số lượng Byte trên một giây là %d" % BytePerSec) #độ rộng mẫu 2 byte, 2 kênh -> 4 bytes

BytePerBloc = f.read(2)
BytePerBloc = BytePerBloc[1]*256 + BytePerBloc[0]
print("Số lượng Byte trên một mẫu là %d" % BytePerBloc) #một khối 2 kênh, mỗi kênh 2 byte (mẫu) -> 4 bytes

BitsPerSample = f.read(2)
BitsPerSample = BitsPerSample[1]*256 + BitsPerSample[0]
print("Số lượng bit của một mẫu là %d" % BitsPerSample) #16 bits = 2 bytes

DataBlocID = f.read(4)
print("%c%c%c%c" % (DataBlocID[0], DataBlocID[1], DataBlocID[2], DataBlocID[3]))

DataSize = f.read(4)
DataSize = DataSize[3]*255**3 + DataSize[2]*256**2 + DataSize[1]*256 + DataSize[0]
print("Data size là %d" % DataSize)

soLuongMau = DataSize // BytePerBloc #1 kênh -> //2, 2 kênh -> //4
print("Số lượng mẫu là %d" % soLuongMau)

f.close()
pass#debug