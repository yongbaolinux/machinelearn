<?php
class matrix{
    
    public function matrixPlus($matrix1,$matrix2){
        if($this->validMatrix($matrix1) == false || $this->validMatrix($matrix2) == false){
            echo 'paramters is invalid';
        } else {
            $matrix1_info = $this->validMatrix($matrix1);
            $matrix2_info = $this->validMatrix($matrix2);
            if($matrix1_info[0] !== $matrix2_info[0] || $matrix1_info[1] !== $matrix2_info[1]){
                echo 'can\t plus';
            } else {
                for($i = 0; $i < $matrix1_info[0];$i++){
                    for($j = 0; $j < $matrix1_info[1];$j++){
                        $matrix3[$i][$j] = $matrix1[$i][$j] + $matrix2[$i][$j];
                    }
                }
                return $matrix3;
            }
        }
        
    }
    
    public function matrixMinus($matrix1,$matrix2){
        if($this->validMatrix($matrix1) == false || $this->validMatrix($matrix2) == false){
            echo 'paramters is invalid';
        } else {
            $matrix1_info = $this->validMatrix($matrix1);
            $matrix2_info = $this->validMatrix($matrix2);
            if($matrix1_info[0] !== $matrix2_info[0] || $matrix1_info[1] !== $matrix2_info[1]){
                echo 'can\t plus';
            } else {
                for($i = 0; $i < $matrix1_info[0];$i++){
                    for($j = 0; $j < $matrix1_info[1];$j++){
                        $matrix3[$i][$j] = $matrix1[$i][$j] - $matrix2[$i][$j];
                    }
                }
                return $matrix3;
            }
        }
    
    }
    
    public function matrixMulti($matrix1,$matrix2){
        if($this->validMatrix($matrix1) == false || $this->validMatrix($matrix2) == false){
            echo 'paramters is invalid';
        } else {
            $matrix1_info = $this->validMatrix($matrix1);
            $matrix2_info = $this->validMatrix($matrix2);
            if($matrix1_info[1] !== $matrix2_info[0]){
                echo 'can\'t multiplication';
            } else {
                for($i = 0; $i < $matrix1_info[0];$i++){
                    for($j = 0; $j < $matrix2_info[1];$j++){
                        for($k = 0; $k < $matrix1_info[1]; $k++){
                            $matrix3[$i][$j] += $matrix1[$i][$k] * $matrix2[$k][$j];
                        }
                    }
                }
                return $matrix3;
            }
        }
    }
    
    private function validMatrix($matrix){
        if(is_array($matrix)){
            $m = count($matrix);
            if($m > 0){
                foreach ($matrix as $k=>$v){
                   if(is_array($v)){
                       if($k > 0){
                           if(count($v) !== count($matrix[$k-1])){
                               return false;
                           }
                       }
                   } else {
                       return false;
                   }
                }
                return [$m,count($v)];
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
    
    public function matrixSwitchRow($matrix,$from=1,$to=1){
        if($this->validMatrix($matrix) == false){
            echo 'the parameter is invalid matrix';
            return false;
        } else {
            if(intval($from) <= 0 || intval($to) <= 0 || $from > count($matrix) || $to > count($matrix)){
                echo 'parmater is invalid';
                return false;
            } else {
                $temp =  $matrix[$to-1];
                $matrix[$to-1] = $matrix[$from-1];
                $matrix[$from-1] = $temp;
            }
        }
        return $matrix;
    }
    
    public function matrixPrint($matrix){
        foreach ($matrix as &$v){
            if(is_array($v)){
                $v = $this->matrixPrint($v);
            }
        }
        echo str_replace(array("[[","]]","],["), array("[\n [","] \n]","],\n ["), '['.implode(",", $matrix).']');
    }

    /**
    **  计算乘方
    **  $base 底数
    **  $exponent 指数
    */
    public function mathPower($base,$exponent){
        $result = 1;
        for($i=$exponent; $i>0; $i--){
            $result *= $base;
        }
        return $result;
    }
    
    /*
    **  计算一个数列的逆序数
    **  12345计为全正序 逆序数为0
    **  $arr 待计算逆序数的数列
    */
    public function mathReverseCount($arr=[]){
        $reverseCount = 0;
        foreach ($arr as $v) {
            array_shift($arr);
            foreach ($arr as $v2) {
                if($v > $v2){
                    $reverseCount++;
                }
            }
        }
        return $reverseCount;                                                                           
    }

    /*
    **  计算一个数列的子数列全组合
    **  $arr 原始数列
    **  $base 子数列的元素个数
    */
    public function mathC($arr=[],$base=3){
        foreach($arr as $k=>$v){
            $arr2 = array_slice($arr, $k+1);
            $temp[0] = $v;
            foreach ($arr2 as $k2 => $v2) {
                $temp[1] = $v2;
                $arr3 = array_slice($arr2, $k2+1);
                //print_r($arr3);exit();
                foreach ($arr3 as $v3) {
                    $temp[2] = $v3;
                    $result[] = $temp;
                }
            }

        }
        return $result;
    }

    // public function mathC_($arr=[],$base){
    //     $base--;
    //     foreach ($arr as $k => $v) {
    //         $arr_temp = array_slice($arr, $k+1);
    //         $temp[0] = $v;
    //         if($base > 1){
    //             $arr_temp = $this->mathC_($arr_temp,$base);
    //         } else {
    //             foreach ($arr_temp as $key => $value) {
    //                 $temp[$base] = $value;
    //                 $result[] = $temp;
    //             }
    //         }
    //     }
    //     return $result;
    // }

    /**
     ** 求一个元素数为m数列的n个元素的全排列详情 数列中没有重复的数据
     ** $base n的值
     */
    public function mathC_($arr=[],$base){
        //$temp = [];
        if($base == 1){
            foreach ($arr as $key => $value) {
                $temp[][0] = $value;
            }
        } else {
            $temp_ = $this->mathC_($arr,$base-1);
            
            for($i = 0; $i < count($temp_)-1; $i++){
                
                for($j = $i+1; $j < count($temp_); $j++){
                    
                    $_temp_ = array_unique(array_merge($temp_[$i],$temp_[$j]));
                    if(count($_temp_) == $base){
                        sort($_temp_);
                        $temp[] = $_temp_;
                    }
                }
            }
            //print_r($temp);
        }
        return $temp;
    }

    /**
     ** 去除二维数组中的重复值
     */
    public function multi_array_unique($arr=[[]]){
        foreach ($arr as $v){
            $v = implode(',',$v);              
               $temp[] = $v;
            }
            $temp = array_unique($temp);
      
        foreach ($temp as $k => $v){
            $temp[$k] = explode(',',$v); 
        }
        return $temp;
    }

    /**
     ** 获取矩阵的某阶子式并计算子式的值是否为0
     ** 如果某阶的所有子式不全为0 则返回true 如果所有某阶子式都为0 则返回false
     ** $n int 子式的阶数
     */  
    public function matrixSon($arr=[],$n=1){
        if($this->validMatrix($arr) == false){
            echo 'the parameter is invalid matrix';
            return false;
        } else {
            $rows_num = count($arr);
            $cols_num = count($arr[0]);
            if($n > $rows_num || $n > $cols_num){
                echo '阶数不能超过矩阵行数或列数';
                return false;
            }
            $rows = range(1, $rows_num);
            $cols = range(1, $cols_num);
            $rows_son = $this->multi_array_unique($this->mathC_($rows,$n));
            $cols_son = $this->multi_array_unique($this->mathC_($cols,$n));
            //print_r($cols_son);
            foreach ($rows_son as $rows_son_key => $row_son) {
                foreach ($cols_son as $cols_son_key => $col_son) {
                    foreach ($row_son as $row_key => $row_value) {
                        foreach ($col_son as $col_key => $col_value) {
                            $son_arr[$row_key][$col_key] = $arr[$row_value-1][$col_value-1];
                        }
                    }
                    if($this->matrixValue($son_arr)){       //判断子式的值是否为0
                        return true;
                    }                      

                }
            }
            return false;
        }
    }

    /**
     ** 计算行列式的值
     */
    public function matrixValue($arr=[]){
        
        $result = 0;
        $arr_ = range(0, count($arr)-1);
        $mathP = $this->mathP($arr_);
        
        foreach($mathP as $value){
            $reverseCount = $this->mathReverseCount($value);
            $desc = $this->mathPower(-1,$reverseCount); //修饰符
            $unit = 1;    
            foreach($value as $k=>$v){
                $unit *= $arr[$k][$v];
            }
            $unit *= $desc;
            $result += $unit;
        }
        return $result;
    }

    /*
     ** 计算一个数列的全排列
     ** n个数的全排列是在 n-1 的基础上再增加 n 种情况
     */
    public function mathP($arr=[]){
        if(count($arr) == 1){
            $result[] = $arr;
        } else {
            $pop = array_pop($arr);
            $result_ = $this->mathP($arr);  //去除数组最后一个元素的全排列集合
            
            foreach ($result_ as $key => $value) {
                
                for($i = 0; $i <= count($value); $i++){
                    $temp = $value;
                    array_splice($temp, $i, 0, array($pop));
                    $result[] = $temp;
                }
            }
        }
        return $result;
    }

    /**
     ** 计算矩阵的秩
     */
    public function matrixRank($arr=[]){
        if($this->validMatrix($arr) == false){
            echo 'the parameter is invalid matrix';
            return false;
        } else {
            //比较行数和列数的大小 较小的那一个即为秩的最大可能值
            $rows_num = count($arr);
            $cols_num = count($arr[0]);
            $max_rank = ($rows_num > $cols_num) ? $cols_num : $rows_num;
            for($i = 1; $i <= $max_rank; $i++){
                if($this->matrixSon($arr,$i) == false){
                    return $i-1;
                }
            }
            return $max_rank;
        }
    }

}
$matrix1 = [[1,2],[4,5]];
$matrix2 = [[1,2,3],[2,3,-5],[4,7,1]];
$matrix3 = [[3,2,0,5,0],[3,-2,3,6,-1],[2,0,1,5,-3],[1,6,-4,-1,4]];

$matrix = new matrix();
//print_r($matrix->matrixPlus($matrix1,$matrix2));
//print_r($matrix->matrixMulti($matrix1,$matrix2));
//print_r($matrix->matrixSwitchRow($matrix2,1,3));

//echo $matrix->matrixPrint($matrix2);
//echo $matrix->mathPower(1,3);
//echo $matrix->mathReverseCount([5,4,3]);
//print_r($matrix->matrixSon($matrix2,3));
//$matrix3 = [[2,3,5]];
//print_r($matrix->mathP($matrix3));
//var_dump($matrix->matrixSon($matrix2,3));
echo $matrix->matrixRank($matrix3);