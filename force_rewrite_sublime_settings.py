
import sublime
import sublime_plugin


class ForceRewriteSublimeSettingsCommand( sublime_plugin.TextCommand ):
    """
        Apparently after build 3141, Sublime Text is not sorting its settings arrays after
        reloading them.
    """

    def run( self, edit ):

        # userPreferences        = sublime.load_settings( 'Preferences.sublime-settings' )
        # packageControlSettings = sublime.load_settings( 'Package Control.sublime-settings' )

        # userPreferences.set( "ForceRewriteSublimeSettings", "0" )
        # packageControlSettings.set( "ForceRewriteSublimeSettings", "0" )

        sublime.save_settings( 'Preferences.sublime-settings' )
        sublime.save_settings( 'Package Control.sublime-settings' )

        # userPreferences.erase( "ForceRewriteSublimeSettings" )
        # packageControlSettings.erase( "ForceRewriteSublimeSettings" )

        # sublime.save_settings( 'Preferences.sublime-settings' )
        # sublime.save_settings( 'Package Control.sublime-settings' )



class ForceReloadSublimeColorScheme( sublime_plugin.TextCommand ):

    def run( self, edit ):

        views   = None
        windows = sublime.windows()

        for window in windows:

            print( "\nWindow id: " + str( window.id() ) )
            views = window.views()

            for view in views:

                print( "\"" + "%-32s" % str( view.name() ) + "\": " + self.view.window().active_view().settings().get("color_scheme") )
                view.settings().erase("color_scheme")



