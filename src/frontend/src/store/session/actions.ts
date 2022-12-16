import { createAsyncThunk } from '@reduxjs/toolkit'
import { sessionAPI } from '../../api/session'
import { TSessionInput } from '../../types/session'
import { sessionPush } from './utils'

export const fetchSession = createAsyncThunk(
	'session/fetchSession',
	async (credentials: TSessionInput) => {
		const token = await sessionAPI.getSession(credentials)
		sessionPush(token)
		return token
	}
)
