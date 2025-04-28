# Doxing Prevention in Android

import android.content.Context;
import android.content.SharedPreferences;

public class DoxingPrevention {

    private static final String PREFS_NAME = "UserPrefs";
    private static final String KEY_USER_DATA = "UserData";

    public static void saveUserData(Context context, String userData) {
        SharedPreferences sharedPreferences = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putString(KEY_USER_DATA, userData);
        editor.apply();
    }

    public static String getUserData(Context context) {
        SharedPreferences sharedPreferences = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
        return sharedPreferences.getString(KEY_USER_DATA, null);
    }

    public static void clearUserData(Context context) {
        SharedPreferences sharedPreferences = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.remove(KEY_USER_DATA);
        editor.apply();
    }
}
