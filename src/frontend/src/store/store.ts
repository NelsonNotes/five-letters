import { configureStore } from '@reduxjs/toolkit'
import userReducer from './user/reducers'
import attemptReducer from './attempt/reducers'
import sessionReducer from './session/reducers'

export const store = configureStore({
	reducer: {
		user: userReducer,
		attempt: attemptReducer,
		session: sessionReducer,
	},
})
