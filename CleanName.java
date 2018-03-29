package com.jingdong.www;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class CleanName {
	public static void main(String[] args) throws Exception {

		/**
		 * 文件名称读取
		 */
		// 读取好盘文件名称，此处是对应盘符的名字
		FileInputStream inputStream_name = new FileInputStream("CART_train_gooddisk_360m/360m_good_train.csv");
		BufferedReader bufferedReader_name = new BufferedReader(new InputStreamReader(inputStream_name));
		ArrayList<String> arraylist_name = new ArrayList<>();
		// String[] strarray_name=new String[2];
		String str_name = null;
		String[] strlist=new String[4];
		String temp=null;
		while ((str_name = bufferedReader_name.readLine()) != null) {
			strlist=str_name.split("_");
//			System.out.println(strlist.length);
			temp=strlist[0]+strlist[1]+strlist[2]+strlist[3];
//			System.out.println(temp);
			arraylist_name.add(temp);
		
		}
		
		/**
		 * 贴标签的数据读取
		 */
		// 读取好盘文件元数据
//				FileInputStream inputStream_data = new FileInputStream("goodAndBad_train_1000/good_source.csv");
//				BufferedReader bufferedReader_data = new BufferedReader(new InputStreamReader(inputStream_data));
//				ArrayList<String> arraylist_data = new ArrayList<>();
//				// String[] strarray_name=new String[2];
//				String str_data = null;
//				while ((str_data = bufferedReader_data.readLine()) != null) {
//					arraylist_data.add(str_data);
//
//				}

		inputStream_name.close();
		bufferedReader_name.close();
//		inputStream_data.close();
//		bufferedReader_data.close();
		
		//输出结果的result部分
		BufferedWriter bw = new BufferedWriter(new FileWriter("CART_train_gooddisk_360m/result_name.txt"));

	     

	      //遍历集合

	      for(String s : arraylist_name){
	    	  
//	    	  //出去了末尾是-1的字符串
//	    	  if(s.contains("-1")){
//	    		  continue;
//	    	  }
	         //写数据

	         bw.write(s);

	         bw.newLine();

	         bw.flush();

	      }
	      bw.close();
	}
}
