package com.jingdong.www;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class BaiduVoteBadDisk {
	
	/**这里面测试的每一组数据都是在后面增加了20个多余的数据的，增加的数据并没有关系。
	 * */
	public static int xunhuan(int diskCount, int vote, ArrayList<String> arraylist, int k) {
		int count = 0;
		int count_1=0;
//		int countgood =0;
//		ArrayList<Double> temp=new ArrayList<>();
		double sum=0.0;
		for (int i = 0; i < diskCount; i++) {
			if (i + vote > diskCount) {
				break;
			} else {
				for (int j = i; (i + vote > diskCount + 1) || (j < vote + i); j++) {
					// 投票主体部分
					Double tempnum = Double.parseDouble(arraylist.get(j + (k - diskCount )));
					sum+=tempnum;
//					if (tempnum!=167.191919754806) {
//						countgood++;
//					}
				}
				
				// 区间内的数目平均数超过一个阈值，这时判断这个硬盘好坏的标志,并且直接跳出循环
//				if ((sum/vote)<-0.3) {
				if ((sum/vote)<0) {
//					System.out.println(sum/vote);
//					System.out.println(vote);
//					System.out.println(sum);
					count++;
					sum=0.0;
					return count;
//					break;
				} else {
					count_1++;
//					System.out.println("这是判断外的"+sum);
					sum=0.0;
				}
				sum=0.0;
//				countgood = 0;
			}
		}
//		System.out.println(count_1++);
		return count;
	
	}

	public static void main(String[] args) throws Exception {
		// BufferedReader是可以按行读取文件，此处文件是决策树的结果文件
//		FileInputStream inputStream = new FileInputStream("Vote/CARTBadDiskPreResult.txt");
		FileInputStream inputStream = new FileInputStream("CART_vote_result/test_360s_pre_gooddisk_0.001.txt");
		// FileInputStream inputStream = new
		// FileInputStream("csvFile/baidu_badtest.csv");

		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
		ArrayList<String> arraylist = new ArrayList<>();
		String[] strarray_score = new String[2];
		String str = null;
		while ((str = bufferedReader.readLine()) != null) {
			strarray_score = str.split(",");
			arraylist.add(strarray_score[1]);

		}
		/**
		 * 文件名称读取
		 */
		// 读取坏盘文件名称，此处是对应盘符的名字
//		FileInputStream inputStream_name = new FileInputStream("Vote/Baidu_BadDiskName.txt");
		FileInputStream inputStream_name = new FileInputStream("beiyesinetvote/360s_gooddisk_name.txt");
		BufferedReader bufferedReader_name = new BufferedReader(new InputStreamReader(inputStream_name));
		ArrayList<String> arraylist_name = new ArrayList<>();
		// String[] strarray_name=new String[2];
		String str_name = null;
		while ((str_name = bufferedReader_name.readLine()) != null) {
			arraylist_name.add(str_name);

		}
	
		// close
		inputStream.close();
		bufferedReader.close();
		inputStream_name.close();
		bufferedReader_name.close();
		/**
		 * 投票TIA部分
		 */
		// String index = "9WK30DHQ";
		String index = "";
		// 统计盘的数量
		int DiskCount = 0;
		// 投票人数
		int vote = 5;
		
		// 每个小区间盘符比较的计数
		int diskCount = 0;
		// 好盘中预测为好盘的数目
//	
//		
		int sum=0;
		for (int k = 0; k < arraylist_name.size(); k++) {
			// nameSpace=strlist[k].split("_");
			if (!arraylist_name.get(k).equals(index)) {
				sum+=xunhuan(diskCount, vote, arraylist, k);
				DiskCount++;
				index = arraylist_name.get(k);
//				System.out.println(arraylist_name.get(k));
				k--;
//				System.out.println(k);
//				System.out.println(diskCount);
//				System.out.println("k是"+k);
//				System.out.println("===========");
				diskCount = 0;
			} else {
				diskCount++;
				continue;
			}
			// System.out.println(diskCount + 1);

			// System.out.println(arraylist_name.get(sum));
			// System.out.println(++count);

		}
		int count =0;
		for (String str_data : arraylist) {
			
			double temp = Double.parseDouble(str_data);
			if(temp>1055.74223142595){
				count++;
			}
		}

	
		System.out.println("总的盘数目" + (DiskCount-1));
		System.out.println("坏盘预测成坏盘的" + sum);
		System.out.println(count);
	}
}
