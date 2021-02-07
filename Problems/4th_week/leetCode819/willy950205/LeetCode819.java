package leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LeetCode819 {
	public String mostCommonWord(String paragraph, String[] banned) {
		
		// 접근 방법 : paragraph의 모든 단어를 쪼개 String 배열로 만들고
		// banned의 모든 String을 ArrayList로 다시 만들었다.
		// 그 이후 모든 단어에서 특수기호를 제외 시킨 후
		// map에 넣어 해당 단어의 빈도를 count하였다.
		// 그 이후 가장 빈도가 높지만 금지 단어가 아닌 단어를
		// 반환하였다.
		
		// 아쉬운 점 : 메모리소모가 다른 사람들에 비해 크다.
		
		String [] arr = paragraph.split(" ");
		Map<String, Integer> map = new HashMap<String, Integer>();
		List<String> bannedArr = new ArrayList<String>();
		String answer ="";
		int max = -1;
		for(String word : banned) {
			bannedArr.add(word);
		}
		
		
		
		for(String word : arr) {
			char check [] = word.toLowerCase().toCharArray();
			word="";
			for(char alph : check) {
				if(alph<97||alph>122) {
					break;
				}
				word+=alph;
			}	
			map.put(word, map.getOrDefault(word, 0)+1);	
		}
		
		for(String key : map.keySet()) {
			if(map.get(key)>max&&!bannedArr.contains(key)) {
				max =map.get(key);
				answer = key;
			}
		}
		
        return answer;
    }
}
