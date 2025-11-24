class Solution {
    public boolean isLongPressedName(String name, String typed) {
        int i = 0 , j = 0;
        while(i < name.length() || j < typed.length()){
            if(i < name.length() && j < typed.length() && (name.charAt(i) == typed.charAt(j))){
                i += 1;
                j += 1;
            }
            else{
                if(j > 0 && j < typed.length() && typed.charAt(j) == typed.charAt(j - 1)){
                    j += 1;
                }
                else{
                    return false;
                }
            }
        }

        if(i != name.length()){
            return false;
        }

        if(j != typed.length()){
            return false;
        }

        return true;

    }
}