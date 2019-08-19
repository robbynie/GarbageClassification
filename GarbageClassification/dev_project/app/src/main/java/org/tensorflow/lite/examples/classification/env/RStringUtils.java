package org.tensorflow.lite.examples.classification.env;

public class RStringUtils {
    public static String getGarbageHandlingAdvise(String title){
        // 可回收
        if (title.indexOf("Newspaper") >= 0) {
            return "<报纸>:废纸张 -> 可回收";
        } else if(title.indexOf("Carton") >= 0) {
            return "<纸箱>:废纸张 -> 可回收";
        } else if(title.indexOf("envelope") >= 0) {
            return "<信封>:废纸张 -> 可回收";
        } else if(title.indexOf("plastic_bottle") >= 0) {
            return "<塑料瓶>:废塑料 -> 可回收";
        } else if(title.indexOf("plastic_toys") >= 0) {
            return "<塑料玩具>:废塑料 -> 可回收";
        } else if(title.indexOf("Crisper_box") >= 0) {
            return "<保鲜盒>:废塑料 -> 可回收";
        } else if(title.indexOf("Wine_bottle") >= 0) {
            return "<酒瓶>:废玻璃 -> 可回收";
        } else if(title.indexOf("glass") >= 0) {
            return "<玻璃杯>:废玻璃 -> 可回收";
        } else if(title.indexOf("Cans") >= 0) {
            return "<易拉罐>:废金属 -> 可回收";
        } else if(title.indexOf("Knife") >= 0) {
            return "<刀>:废金属 -> 可回收";
        } else if(title.indexOf("leather shoes") >= 0) {
            return "<皮鞋>:废织物 -> 可回收";
        } else if(title.indexOf("package") >= 0) {
            return "<包>:废织物 -> 可回收";
        }

        // 有害垃圾
        if (title.indexOf("Battery") >= 0) {
            return "<电池>:有害垃圾 -> 不可回收";
        } else if(title.indexOf("Pharmaceutical_Packaging") >= 0) {
            return "<药品包装>:有害垃圾 -> 不可回收";
        } else if(title.indexOf("Pill") >= 0) {
            return "<药片>:有害垃圾 -> 不可回收";
        } else if(title.indexOf("Insecticide_spray") >= 0) {
            return "<杀虫喷剂>:有害垃圾 -> 不可回收";
        } else if(title.indexOf("Expired_capsule_drug") >= 0) {
            return "<胶囊药物>:有害垃圾 -> 不可回收";
        }

        // 湿垃圾
        if (title.indexOf("Meanls") >= 0) {
            return "<剩饭剩菜>:湿垃圾 -> 不可回收";
        } else if(title.indexOf("bread") >= 0) {
            return "<面包>:湿垃圾 -> 不可回收";
        } else if(title.indexOf("Cake biscuit") >= 0) {
            return "<饼干>:湿垃圾 -> 不可回收";
        } else if(title.indexOf("Dried nuts") >= 0) {
            return "<干果仁>:湿垃圾 -> 不可回收";
        } else if(title.indexOf("Pet feed") >= 0) {
            return "<宠物饲料>:湿垃圾 -> 不可回收";
        } else if(title.indexOf("flowers") >= 0) {
            return "<花卉>:湿垃圾 -> 不可回收";
        }

        // 干垃圾
        if (title.indexOf("Napkin") >= 0) {
            return "<餐巾纸>:干垃圾 -> 可回收";
        } else if(title.indexOf("toilet_paper") >= 0) {
            return "<厕纸>:干垃圾 -> 不可回收";
        } else if(title.indexOf("Cigarette") >= 0) {
            return "<烟头>:干垃圾 -> 不可回收";
        } else if(title.indexOf("tape") >= 0) {
            return "<胶带>:干垃圾 -> 不可回收";
        } else if(title.indexOf("Bandage") >= 0) {
            return "<创口贴>:干垃圾 -> 不可回收";
        } else if(title.indexOf("pen") >= 0) {
            return "<笔>:干垃圾 -> 不可回收";
        } else if(title.indexOf("towel") >= 0) {
            return "<旧毛巾>:干垃圾 -> 不可回收";
        } else if(title.indexOf("Underwear") >= 0) {
            return "<内衣裤>:干垃圾 -> 不可回收";
        } else if(title.indexOf("Garbage_plastic_bag") >= 0) {
            return "<塑料垃圾袋>:干垃圾 -> 不可回收";
        }

        return title;
    }
}
