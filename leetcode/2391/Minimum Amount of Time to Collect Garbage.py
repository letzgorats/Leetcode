class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        
        g_truck, g_idx = 0, 0 
        p_truck, p_idx = 0, 0 
        m_truck, m_idx = 0, 0

        for idx,t in enumerate(garbage):

            if "G" in t:
                g_truck += t.count("G")
                g_idx = idx
            if "P" in t:
                p_truck += t.count("P")
                p_idx = idx
            if "M" in t:
                m_truck += t.count("M")
                m_idx = idx

        g_truck += sum(travel[:g_idx])
        p_truck += sum(travel[:p_idx])
        m_truck += sum(travel[:m_idx])
    
        return g_truck + p_truck + m_truck
