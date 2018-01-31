class IP4Address:
    ip_address=[0,0,0,0]
    mask      = 0

    def __init__(self,ip_address,mask):
        self.ip_address = ip_address
        self.mask = mask

    def getMask(self):
        list_octat = [128,64,32,16,8,4,2,1]
        list_result = [0,0,0,0]
        sum_octat = 0
        index = 0
        sum_max = 1020

        for i in range(self.mask):
                sum_octat = list_octat[index] + sum_octat
                index = index + 1
                if(index>7):
                    index = 0
        sum_diff = sum_max-sum_octat
        check_var = sum_octat//255

        for i in range(check_var):
            list_result[i] = 255
        if(sum_diff<255):
                list_result[3]=255 - (sum_diff)
        print(list_result)

ipv4 = IP4Address([10,0,0,0],26)
ipv4.getMask()