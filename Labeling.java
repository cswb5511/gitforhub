package com.jingdong.www;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class Labeling {
	
	/**由于判断盘符的原因，要在每个文件后面加10个无关的文件
	 * */
	static int sum = 0;
	
	public static ArrayList<String> tieBiaoQian(int sum,int k,ArrayList<String> arraylist_data,int count,int diskCount){
//		String[] ar=new String[14];
//		System.out.println("count是"+count);
//		System.out.println("diskCount是"+diskCount);
//		int show =diskCount-count;
//		System.out.println("diskCount-count是"+show);
		//直接分解读取的文件
//		ar=arraylist_data.split(",");
//		double all=1/(diskCount-count);
		//String all="1/"+(diskCount-count);
		for (int i = 0; i < diskCount-count; i++) {
			//这里面截取最后两位，是因为坏盘都-1需要2位
			//double temp=-1.0+(diskCount-count-i+0.0)/(diskCount-count);
			double temp=(diskCount-count+0.0-i);
			arraylist_data.set(count+i+(sum-diskCount),arraylist_data.get(count+i+(sum-diskCount)).substring(0,arraylist_data.get(count+i+(sum-diskCount)).length()-2)+temp+"");
			//ar[13]=Integer.toString(all);
			
		}
//		System.out.println("替代的末尾"+arraylist_data.get(k+count));
		return arraylist_data;
	
//		StringBuffer sb = new StringBuffer();
//		for(int i = 0; i < ar.length; i++){
//		 sb. append(ar[i]);
//		}
//		String s = sb.toString();
//		System.out.println(s);
	}
	
	public static ArrayList<String> xunhuan(int diskCount, int vote, ArrayList<String> arraylist, int k,int sum,ArrayList<String> arraylist_data) {
		int countgood = 0;
		ArrayList<String> data = null;
		for (int i = 0; i < diskCount; i++) {
			if (i + vote > diskCount) {
				break;
			} else {
				for (int j = i; (i + vote > diskCount + 1) || (j < vote + i); j++) {
					// 投票主体部分
					int tempnum = Integer.parseInt(arraylist.get(j + (k - diskCount )));
//					 System.out.print("输出一下");
//					 System.out.println(j + (k - diskCount ));
//					 System.out.println(tempnum);
					if (tempnum == -1) {
						countgood++;
					}
				}
				// 如果出现的条目的好的连续的条目不超过投票人数的一半即大于等于3那么这个盘就是被判断为坏盘
				if (countgood >= ((vote + 1) / 2)) {
					data=tieBiaoQian(sum, k, arraylist_data,countgood,diskCount);
					countgood=0;
					break;
				} else {
					// 只要有一次连续5个中有3个是坏盘的那就是判为坏盘，判定这个盘符就是坏盘了后面无需判断

				}
				countgood = 0;
			}
		}
		return data;
	}

	public static void main(String[] args) throws Exception {
		// BufferedReader是可以按行读取文件，此处文件是决策树的结果文件
		//FileInputStream inputStream = new FileInputStream("CART_train_baddisk_360m/360m_badtrain_score_idents.csv");
		FileInputStream inputStream = new FileInputStream("testCART/baidu_badtrain_score_idents.csv");
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
		// 读取坏盘文件名称，此处是对应盘符的名字
//		FileInputStream inputStream_name = new FileInputStream("CART_train_baddisk_360m/360s_badtrain_name.txt");
//		FileInputStream inputStream_name = new FileInputStream("CART_train_baddisk_360m/360m_badtrain_name.txt");
		FileInputStream inputStream_name = new FileInputStream("testCART/baidu_badtrain_name.txt");
		BufferedReader bufferedReader_name = new BufferedReader(new InputStreamReader(inputStream_name));
		ArrayList<String> arraylist_name = new ArrayList<>();
		// String[] strarray_name=new String[2];
		String str_name = null;
		while ((str_name = bufferedReader_name.readLine()) != null) {
			arraylist_name.add(str_name);

		}
		/**
		 * 贴标签的数据读取
		 */
		// 读取坏盘文件名称
			//	FileInputStream inputStream_data = new FileInputStream("CART_train_baddisk_360s/360s_source_bad.csv");
			//	FileInputStream inputStream_data = new FileInputStream("CART_train_baddisk_360m/360m_source_bad.csv");
				FileInputStream inputStream_data = new FileInputStream("testCART/baidu_source.txt");
				BufferedReader bufferedReader_data = new BufferedReader(new InputStreamReader(inputStream_data));
				ArrayList<String> arraylist_data = new ArrayList<>();
				// String[] strarray_name=new String[2];
				String str_data = null;
				while ((str_data = bufferedReader_data.readLine()) != null) {
					arraylist_data.add(str_data);

				}
		// close
		inputStream.close();
		bufferedReader.close();
		inputStream_name.close();
		bufferedReader_name.close();
		inputStream_data.close();
		bufferedReader_data.close();
		/**
		 * 投票TIA部分
		 */
		// String index = "9WK30DHQ";
		String index = "";
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
		//	最后输出的list
		ArrayList<String> data = null;
		for (int k = 0; k < arraylist_name.size(); k++) {
			// nameSpace=strlist[k].split("_");
			if (!arraylist_name.get(k).equals(index)) {
				sum=sum+diskCount;
				data=xunhuan(diskCount, vote, arraylist, k,sum,arraylist_data);
				DiskCount++;
				index = arraylist_name.get(k);
				System.out.println(arraylist_name.get(k));
				k--;
				System.out.println(k);
				System.out.println(diskCount);
				System.out.println("sum是"+sum);
				System.out.println("k是"+k);
				System.out.println("===========");
				diskCount = 0;
			} else {
				diskCount++;
				continue;
			}
			// System.out.println(diskCount + 1);

			// System.out.println(arraylist_name.get(sum));
			// System.out.println(++count);

		}
		//输出结果的result部分
		BufferedWriter bw = new BufferedWriter(new FileWriter("testCART/resule_baidu_GBRT.txt"));

	     

	      //遍历集合

	      for(String s : data){
	    	  
	    	  //出去了末尾是-1的字符串
	    	  if(s.contains("-1")){
	    		  continue;
	    	  }
	         //写数据

	         bw.write(s);

	         bw.newLine();

	         bw.flush();

	      }
	      bw.close();

//		System.out.println("总的盘数目" + DiskCount);
//		System.out.println("判断错的条目" + ingoodpropbad);
//		System.out.println("另一个参数" + countgood);
//		System.out.println(sum);
//		
	}
}
