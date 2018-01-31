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
        return(list_result)

    def getWildcard(self,list_arg):
        list1 = []
        for x in list_arg:
            list1.append((255-x))
        return list1

    def getNetwork(self):
        list_octet = [256,128,64,32,16,8,4,2]
        sub_diff = self.mask%8
        num_subnets = 2**(self.mask%8)
        list_network = self.ip_address
        magic_num = list_octet[sub_diff]
        x = magic_num
        while magic_num<=256:
            if int(list_network[3]) < magic_num :
                list_network[3]=magic_num-x
                break
            magic_num=magic_num+x
        return(list_network)






ipv4 = IP4Address([192,168,45,252],26)
list_netmask = (ipv4.getMask())
list_wildcard = ipv4.getWildcard(list_netmask)
list_network = ipv4.getNetwork()

