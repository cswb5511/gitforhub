package com.jingdong.www;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class TieBiaoQian_Baidu {
	static int sum = 0;

	public static void main(String[] args) throws Exception {
		// BufferedReader是可以按行读取文件
		FileInputStream inputStream = new FileInputStream("csvFile/baidu_badtest_score_idents.csv");
		// FileInputStream inputStream = new
		// FileInputStream("csvFile/baidu_badtest.csv");

		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
		ArrayList<String> arraylist = new ArrayList<>();
		String[] strarray_score = new String[2];
		String str = null;
		while ((str = bufferedReader.readLine()) != null) {
			strarray_score = str.split(",");
			arraylist.add(strarray_score[1].replace("\"", "").replace("\"", ""));

		}
		/**
		 * 文件名称读取
		 */
		// 读取坏盘文件名称
		FileInputStream inputStream_name = new FileInputStream("csvFile/bad_test_name.txt");
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
		String index = "9WK30DHQ";
		// 统计盘的数量
		int DiskCount = 0;
		// 投票人数
		int vote = 7;
		// 每个小区间盘符比较的计数
		int diskCount = 0;
		// 投票使用的good标签大于bad标签概率的标记
		int countgood = 0;
		// 投票使用的bad标签大于good标签概率的标记
		int countbad = 0;
		int ingoodpropbad = 0;
		for (int k = 0; k < arraylist_name.size(); k++) {
			// nameSpace=strlist[k].split("_");
			if (!arraylist_name.get(k).equals(index)) {

				DiskCount++;
				index = arraylist_name.get(k);
			} else {
				diskCount++;
				continue;
			}
			System.out.println(diskCount + 1);
			
			//System.out.println(arraylist_name.get(sum));
			// System.out.println(++count);
			if (DiskCount == 1) {
				// 如果是第一个磁盘那么diskCount就不用+1，因为第一次跳过没有少条目
				sum = sum + diskCount ;
				for (int i = 0; i < diskCount ; i++) {
					if (i + vote > diskCount ) {
						break;
					} else {
						for (int j = i; (i + vote > diskCount + 1) || (j < vote + i); j++) {
							// 投票主体部分
							int tempnum = Integer.parseInt(arraylist.get(j + k - sum ));
							System.out.print("输出一下");
							System.out.println(j + k - sum);
							if (tempnum == -1) {
								countgood++;
							}
						}
						// 如果出现的条目的好的连续的条目不超过投票人数的一半即大于等于3那么这个盘就是被判断为坏盘
						if (countgood >= ((vote + 1) / 2)) {
							break;
						} else {
							// 只要有一次连续5个中有3个是坏盘的那就是判为坏盘，判定这个盘符就是坏盘了后面无需判断
							ingoodpropbad++;
							
						}
						countgood = 0;
					}
				}
			} else {
				sum = sum + diskCount +1;
				// 循环开始,+1是因为每一次的if判断会少判断一个条目
				for (int i = 0; i < diskCount + 1; i++) {
					if (i + vote > diskCount + 1) {
						break;
					} else {
						for (int j = i; (i + vote > diskCount + 1) || (j < vote + i); j++) {
							// 投票主体部分
							int tempnum = Integer.parseInt(arraylist.get(j + k ));
							System.out.print("第二遍输出");
							System.out.println(j+k);
							System.out.println(tempnum);
							System.out.println(sum);
							if (tempnum == -1) {
								countgood++;
							}
						}
						// 如果有超过投票的人数判定这个盘是坏盘，那么它就是坏盘了
						if (countgood >= ((vote + 1) / 2)) {
							countgood = 0;
							break;
						} else {
							// 只要有一次连续5个中有3个是坏盘的那就是判为坏盘，判定这个盘符就是坏盘了后面无需判断
							ingoodpropbad++;
						
						}
						
					}
				}
			}
			System.out.println("内部循环的小区间" + diskCount);
			diskCount = 0;

		}
		System.out.println("总的盘数目" + DiskCount);
		System.out.println("判断错的条目" + ingoodpropbad);
		System.out.println("另一个参数" + countgood);
		System.out.println(sum);
		System.out.println(arraylist.get(17699));
	}
}
